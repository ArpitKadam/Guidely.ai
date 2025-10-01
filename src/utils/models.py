import os
from typing import Any, Optional
from pydantic import BaseModel, Field
import yaml
from src.logger import logger
from src.exception import CustomException
from dotenv import load_dotenv

load_dotenv()

try:
    from langchain_groq import ChatGroq
except ImportError:
    ChatGroq = None
    logger.error("langchain_groq is not installed. Please install it before using Groq LLM.")


class ConfigLoader:
    """
    Loads and provides access to configuration values from a YAML file.

    Example:
        config = ConfigLoader("src/config/config.yaml")
        model_name = config["llm"]["groq"]["model_name"]
    """

    def __init__(self, config_path: str = "src/config/config.yaml"):
        self.config_path = config_path
        try:
            with open(config_path, "r") as file:
                self.config = yaml.safe_load(file) or {}
            logger.info(f"✅ Configuration loaded successfully from {config_path}")
        except FileNotFoundError:
            logger.exception(f"❌ Configuration file not found at {config_path}")
            raise CustomException(f"Configuration file not found: {config_path}")
        except yaml.YAMLError as e:
            logger.exception(f"❌ Failed to parse YAML configuration from {config_path}")
            raise CustomException(f"YAML parsing error: {e}")
        except Exception as e:
            logger.exception(f"❌ Unexpected error while loading config from {config_path}")
            raise CustomException(f"Unexpected error: {e}")

    def __getattr__(self, key: str):
        """Allow attribute-style access to config dictionary."""
        return self.config.get(key)

    def __getitem__(self, key: str):
        """Allow dictionary-style access to config dictionary."""
        return self.config.get(key)


class ModelLoader(BaseModel):
    """
    Loads and returns the Groq LLM model using the configuration defined in `config.yaml`.
    """

    config: Optional[ConfigLoader] = Field(default=None, exclude=True)

    class Config:
        arbitrary_types_allowed = True

    def model_post_init(self, __context: Any) -> None:
        """Ensure configuration is loaded after initialization."""
        try:
            if self.config is None:
                self.config = ConfigLoader()
            logger.debug("ConfigLoader initialized inside ModelLoader.")
        except Exception as e:
            logger.exception("❌ Failed to initialize ConfigLoader inside ModelLoader")
            raise CustomException(f"Config initialization failed: {e}")

    def load_llm(self):
        """
        Load and return the Groq LLM instance.

        Returns:
            ChatGroq: Initialized Groq chat model instance.

        Raises:
            CustomException: If required configuration or dependencies are missing.
        """
        try:
            if self.config is None:
                self.config = ConfigLoader()

            # Extract model name safely
            model_name = (
                self.config['llm']['groq']['model_name']
            )

            if not model_name:
                logger.error("❌ 'model_name' missing in config under llm.groq")
                raise CustomException("Groq model_name not found in config.yaml")

            if ChatGroq is None:
                raise ImportError("langchain_groq is not installed.")

            # Load API Key
            groq_api_key = os.getenv("GROQ_API_KEY")
            if not groq_api_key:
                logger.warning("⚠️ GROQ_API_KEY not found in environment variables.")

            logger.info(f"🔄 Loading Groq LLM with model: {model_name}")
            llm = ChatGroq(model=model_name, api_key=groq_api_key)
            logger.info("✅ Groq LLM loaded successfully.")
            return llm

        except ImportError as e:
            logger.exception("❌ Missing dependency for Groq LLM.")
            raise CustomException(f"Dependency error: {e}")
        except Exception as e:
            logger.exception("❌ Failed to load Groq LLM.")
            raise CustomException(f"Error loading Groq LLM: {e}")
