const CHAT_KEY = "guidely_chat_v1"
const THEME_KEY = "guidely_theme"

const $ = (sel) => document.querySelector(sel)
const chatEl = $("#chat")
const inputEl = $("#chat-input")
const formEl = $("#chat-form")
const submitEl = $("#chat-submit")
const clearEl = $("#chat-clear")
const yearEl = document.getElementById("year")
const toggle = document.getElementById("theme-toggle")
const toggleText = document.querySelector("#theme-toggle .theme-toggle-text")
const showBtn = document.getElementById("show-links-md")
const dlBtn = document.getElementById("download-links-md")
const copyBtn = document.getElementById("copy-links-md")
const panel = document.getElementById("links-md-panel")
const textarea = document.getElementById("links-md-text")

// Footer year
if (yearEl) yearEl.textContent = new Date().getFullYear().toString()

// Load and save chat history
function loadChat() {
  try {
    return JSON.parse(localStorage.getItem(CHAT_KEY) || "[]")
  } catch {
    return []
  }
}
function saveChat(messages) {
  localStorage.setItem(CHAT_KEY, JSON.stringify(messages))
}

function formatTimestamp(d = new Date()) {
  return new Intl.DateTimeFormat(undefined, {
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
  }).format(d)
}

function renderMessages(messages) {
  if (!chatEl) return
  chatEl.innerHTML = ""
  for (const m of messages) {
    chatEl.appendChild(renderMessage(m))
  }
  chatEl.scrollTop = chatEl.scrollHeight
}

function renderMessage({ role, content, ts }) {
  const wrapper = document.createElement("div")
  wrapper.className = `msg ${role === "user" ? "user" : "assistant"}`

  const bubble = document.createElement("div")
  bubble.className = "bubble"
    // Render Markdown if assistant, plain text if user
  if (role === "assistant") {
    bubble.innerHTML = marked.parse(content)
  } else {
    bubble.textContent = content
  }

  const meta = document.createElement("div")
  meta.className = "meta"
  meta.textContent = `${role === "user" ? "You" : "Guidely.ai"} • ${formatTimestamp(new Date(ts))}`

  wrapper.appendChild(bubble)
  wrapper.appendChild(meta)
  return wrapper
}

function addMessage(role, content) {
  const messages = loadChat()
  const msg = { role, content, ts: new Date().toISOString() }
  messages.push(msg)
  saveChat(messages)
  renderMessages(messages)
  return msg
}

function setLoading(loading) {
  if (!submitEl) return
  submitEl.disabled = loading
  submitEl.textContent = loading ? "Thinking…" : "Send"
  inputEl.disabled = loading
}

async function sendQuery(query) {
  try {
    const res = await fetch("/query", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query }),
    })
    const data = await res.json()
    if (!res.ok) {
      throw new Error(data?.error || "Unknown error")
    }
    return data?.answer || "No answer returned."
  } catch (err) {
    throw err
  }
}

function applyTheme(theme) {
  const htmlEl = document.documentElement
  if (theme === "dark") {
    htmlEl.classList.add("dark")
  } else {
    htmlEl.classList.remove("dark")
  }
  if (toggle) {
    toggle.setAttribute("aria-pressed", theme === "dark" ? "true" : "false")
    if (toggleText) toggleText.textContent = theme === "dark" ? "Light" : "Dark"
    toggle.setAttribute("aria-label", theme === "dark" ? "Switch to light mode" : "Switch to dark mode")
  }
}

function getPreferredTheme() {
  const saved = localStorage.getItem(THEME_KEY)
  if (saved === "light" || saved === "dark") return saved
  // system preference fallback
  return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light"
}

document.addEventListener("DOMContentLoaded", () => {
  // Apply initial theme
  applyTheme(getPreferredTheme())

  // Contact page markdown wiring
  const linksMarkdown = `[![Personal Website](https://img.shields.io/badge/Personal-4CAF50?style=for-the-badge&logo=googlechrome&logoColor=white)](https://arpit-kadam.netlify.app/)
[![Gmail](https://img.shields.io/badge/gmail-D14836?&style=for-the-badge&logo=gmail&logoColor=white)](mailto:arpitkadam922@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?&style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/arpitkadam/)
[![DAGsHub](https://img.shields.io/badge/DAGsHub-231F20?style=for-the-badge&logo=dagshub&logoColor=white)](https://dagshub.com/ArpitKadam)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?&style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/arpitkadam5)
[![Dev.to](https://img.shields.io/badge/Dev.to-0A0A0A?&style=for-the-badge&logo=dev.to&logoColor=white)](https://dev.to/arpitkadam)
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?&style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/arpitkadam)
[![Instagram](https://img.shields.io/badge/Instagram-E1306C?&style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/arpit__kadam/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?&style=for-the-badge&logo=github&logoColor=white)](https://github.com/arpitkadam)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-FB7A1E?style=for-the-badge&logo=buymeacoffee&logoColor=white)](https://buymeacoffee.com/arpitkadam)`

  if (textarea) textarea.value = linksMarkdown

  if (showBtn && panel) {
    showBtn.addEventListener("click", () => {
      const willShow = panel.hasAttribute("hidden")
      if (willShow) {
        panel.removeAttribute("hidden")
        panel.setAttribute("aria-hidden", "false")
        showBtn.setAttribute("aria-expanded", "true")
      } else {
        panel.setAttribute("hidden", "")
        panel.setAttribute("aria-hidden", "true")
        showBtn.setAttribute("aria-expanded", "false")
      }
    })
  }

  if (copyBtn && textarea) {
    copyBtn.addEventListener("click", async () => {
      textarea.select()
      try {
        await navigator.clipboard.writeText(textarea.value)
        copyBtn.textContent = "Copied!"
        setTimeout(() => (copyBtn.textContent = "Copy"), 1200)
      } catch {
        // fallback
        document.execCommand("copy")
      }
    })
  }

  if (dlBtn) {
    dlBtn.addEventListener("click", () => {
      const blob = new Blob([linksMarkdown], { type: "text/markdown;charset=utf-8" })
      const url = URL.createObjectURL(blob)
      const a = document.createElement("a")
      a.href = url
      a.download = "important-links.md"
      document.body.appendChild(a)
      a.click()
      a.remove()
      URL.revokeObjectURL(url)
    })
  }

  // Wire toggle button
  if (toggle) {
    toggle.addEventListener("click", () => {
      const next = document.documentElement.classList.contains("dark") ? "light" : "dark"
      localStorage.setItem(THEME_KEY, next)
      applyTheme(next)
    })
  }

  renderMessages(loadChat())

  if (formEl) {
    formEl.addEventListener("submit", async (e) => {
      e.preventDefault()
      const query = (inputEl.value || "").trim()
      if (!query) return

      // Add user message
      addMessage("user", query)

      // Add temp assistant message (spinner feel)
      const placeholder = addMessage("assistant", "✨ Crafting your personalized travel plans...")

      // Lock UI during request
      setLoading(true)

      try {
        const answer = await sendQuery(query)
        // Replace last assistant placeholder message with final answer
        const messages = loadChat()
        // Find and replace last assistant (placeholder)
        for (let i = messages.length - 1; i >= 0; i--) {
          if (messages[i].role === "assistant" && messages[i].content.includes("Crafting your personalized")) {
            const generatedAt = formatTimestamp(new Date())
            messages[i].content = `Guidely.ai Travel Plan\n\nGenerated: ${generatedAt}\n\n${answer}`
            messages[i].ts = new Date().toISOString()
            break
          }
        }
        saveChat(messages)
        renderMessages(messages)
      } catch (err) {
        // Replace placeholder with error
        const messages = loadChat()
        for (let i = messages.length - 1; i >= 0; i--) {
          if (messages[i].role === "assistant" && messages[i].content.includes("Crafting your personalized")) {
            messages[i].content = `❌ Bot failed to respond: ${err?.message || err}`
            messages[i].ts = new Date().toISOString()
            break
          }
        }
        saveChat(messages)
        renderMessages(messages)
      } finally {
        setLoading(false)
        inputEl.value = ""
        inputEl.focus()
      }
    })
  }

  if (clearEl) {
    clearEl.addEventListener("click", () => {
      localStorage.removeItem(CHAT_KEY)
      renderMessages([])
      inputEl?.focus()
    })
  }
})
