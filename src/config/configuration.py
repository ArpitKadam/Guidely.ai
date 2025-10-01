import os
import yaml
from src.logger import logger
from src.exception import CustomException


def load_config(config_path: str = "src/config/config.yaml") -> dict:
    """
    Load YAML configuration file.

    Parameters
    ----------
    config_path : str, optional
        Path to the YAML config file. Default is 'src/config/config.yaml'.

    Returns
    -------
    dict
        Dictionary containing configuration values.

    Raises
    ------
    CustomException
        If the configuration file cannot be read or parsed.
    """
    try:
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file not found at {config_path}")

        with open(config_path, "r") as file:
            config = yaml.safe_load(file)

        logger.info(f"Configuration loaded successfully from {config_path}")
        return config

    except Exception as e:
        logger.exception("Failed to load configuration")
        raise CustomException(f"Error loading configuration: {e}")
