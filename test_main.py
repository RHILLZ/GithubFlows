import pytest
import os
from unittest.mock import patch
import logging
from main import main


@pytest.fixture(autouse=True)
def setup_logging():
    """Setup logging for tests"""
    # Clear any existing handlers
    logger = logging.getLogger("main")
    logger.handlers = []

    # Set up new handlers
    file_handler = logging.FileHandler("app.log")
    stream_handler = logging.StreamHandler()
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.setLevel(logging.INFO)

    yield

    # Clean up
    logger.handlers = []


def test_logging_setup():
    """Test if logging is properly configured"""
    logger = logging.getLogger("main")
    assert logger.level == logging.INFO
    assert len(logger.handlers) == 2


def test_main_function(caplog):
    """Test the main function's logging output"""
    caplog.set_level(logging.INFO)
    test_key = "test123"
    with patch.dict(os.environ, {"SECRET_KEY": test_key}, clear=True):
        with patch("main.secret_key", test_key):
            main()

    # Check if the expected log messages are present
    assert "Starting application" in caplog.text
    assert f"Secret key loaded: {'*' * len(test_key)}" in caplog.text
    assert "Application completed" in caplog.text


def test_main_function_no_secret_key(caplog):
    """Test the main function when no secret key is present"""
    caplog.set_level(logging.INFO)
    with patch.dict(os.environ, {}, clear=True):
        with patch("main.secret_key", None):
            main()

    # Check if the expected log messages are present
    assert "Starting application" in caplog.text
    assert "Secret key loaded: None" in caplog.text
    assert "Application completed" in caplog.text
