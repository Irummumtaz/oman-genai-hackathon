import logging
import sys
from datetime import datetime
import json


class StructuredFormatter(logging.Formatter):
    """
    Custom formatter that outputs logs in a structured JSON format.
    """

    def format(self, record):
        log_data = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }

        # Add exception info if present
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)

        # Add any extra fields passed via extra parameter
        if hasattr(record, "extra_fields"):
            log_data.update(record.extra_fields)

        return json.dumps(log_data)


def setup_logging(level=logging.INFO, json_format=False):
    """
    Set up structured logging for the application.

    Args:
        level: Logging level (default: INFO)
        json_format: If True, use JSON formatting; otherwise use readable format
    """
    root_logger = logging.getLogger()

    # Remove existing handlers
    root_logger.handlers.clear()

    # Create console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)

    # Set formatter based on preference
    if json_format:
        formatter = StructuredFormatter()
    else:
        # Readable structured format
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)
    root_logger.setLevel(level)

    return root_logger


def get_logger(name):
    """
    Get a logger instance with the specified name.

    Args:
        name: Name of the logger (typically __name__)

    Returns:
        logging.Logger instance
    """
    return logging.getLogger(name)
