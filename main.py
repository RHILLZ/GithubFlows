import os
import logging
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

load_dotenv()

secret_key = os.getenv("SECRET_KEY")


def main():
    logger.info("Starting application")
    if secret_key:
        logger.info(f"Secret key loaded: {'*' * len(secret_key)}")
    else:
        logger.info("Secret key loaded: None")
    logger.info("Application completed")


if __name__ == "__main__":
    main()
