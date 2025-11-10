import argparse
import os
from app.crew import HRCrew
from app.tools.pdf_reader import PDFReaderTool
from app.logging_config import setup_logging, get_logger

# Setup logging
setup_logging()
logger = get_logger(__name__)



def run():

    inputs = {"pdf_files_path":"CV",
              "txt_files_path": "preprocessed-CVs",
              "json_files_path":"processed-CVs",
              "matches_output_path":"job-matches-results"
              }
    logger.info("Running HRCrew", extra={"extra_fields": {"inputs": inputs}})
    try:
        results = HRCrew().crew().kickoff(inputs=inputs)
        return results
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    results = run()
    logger.info("Crew run completed")
    logger.info("Token usage report", extra={"extra_fields": {"token_usage": str(results.token_usage)}})