from app.crew import HRCrew


def run():
    inputs = {
        "pdf_files_path": "CV",
        "txt_files_path": "preprocessed-CVs",
        "json_files_path": "processed-CVs",
        "matches_output_path": "job-matches-results",
    }
    try:
        results = HRCrew().crew().kickoff(inputs=inputs)
        return results
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    results = run()
