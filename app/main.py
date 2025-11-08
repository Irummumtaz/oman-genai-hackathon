import argparse
import os
from app.crew import HRCrew
from app.tools.pdf_reader import PDFReaderTool



def run():

    inputs = {"pdf_files_path":"PDFCVs",
              "txt_files_path": "preprocessed-CVs",
              "json_files_path":"processed-CVs"
              }    
    print(f"Running HRCrew with inputs: {inputs}")
    try:
        results = HRCrew().crew().kickoff(inputs=inputs)
        return results
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    results = run()
    print("Crew run completed.")
    print("\n====================\n")
    print(f"\nToken Usage:\n{results.token_usage}\n")