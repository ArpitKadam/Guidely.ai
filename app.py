import os
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    # Configure backend URL for the FastAPI service
    app.config["BACKEND_URL"] = os.getenv("BACKEND_URL", "http://localhost:8000")

    @app.route("/")
    def index():
        return render_template("index.html", project_name="guidely.ai")

    @app.route("/about")
    def about():
        return render_template("about.html", project_name="guidely.ai")

    @app.route("/features")
    def features():
        return render_template("features.html", project_name="guidely.ai")

    @app.route("/contact")
    def contact():
        return render_template("contact.html", project_name="guidely.ai")

    @app.route("/query", methods=["POST"])
    def query():
        """
        Proxy endpoint: forwards the user's query to the FastAPI backend and returns the answer.
        """
        data = request.get_json(silent=True) or {}
        user_query = (data.get("query") or "").strip()

        if not user_query:
            return jsonify({"error": "Query cannot be empty."}), 400

        try:
            resp = requests.post(
                f"{app.config['BACKEND_URL'].rstrip('/')}/query",
                json={"query": user_query},
                timeout=60,
            )
        except requests.RequestException as e:
            return jsonify({"error": f"Failed to reach backend: {e}"}), 502

        if resp.status_code != 200:
            # Bubble up backend error text
            try:
                return jsonify({"error": resp.json().get("detail", resp.text)}), resp.status_code
            except Exception:
                return jsonify({"error": resp.text}), resp.status_code

        try:
            payload = resp.json()
        except Exception:
            return jsonify({"error": "Invalid JSON from backend."}), 502

        answer = payload.get("answer", "No answer returned.")
        return jsonify({"answer": answer}), 200

    return app


if __name__ == "__main__":
    app = create_app()
    # Default Flask dev server on 5000
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=True)
