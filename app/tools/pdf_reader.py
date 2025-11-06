from crewai.tools import BaseTool
from typing import Type, Optional
from pydantic import BaseModel, Field
import os
import PyPDF2

class PDFReaderToolInput(BaseModel):
    """Input schema for PDFReaderTool."""
    file_path: str = Field(..., description="The path to the PDF file to read")
    output_dir: Optional[str] = Field(None, description="Directory to save the extracted text file")

class PDFReaderTool(BaseTool):
    name: str = "PDF Reader"
    description: str = (
        "Reads and extracts text content from PDF files. "
        "Provide the file path to the PDF document and optionally specify an output directory"
    )
    args_schema: Type[BaseModel] = PDFReaderToolInput

    def _run(self, file_path: str, output_dir: Optional[str] = None) -> str:
        """Extract text from a PDF file and save to output_dir if specified."""
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"

                if not text.strip():
                    return "Error: Could not extract text from PDF. The file might be empty or image-based."

                # Save extracted text if output_dir is provided
                if output_dir:
                    os.makedirs(output_dir, exist_ok=True)
                    base_name = os.path.basename(file_path)
                    file_name = os.path.splitext(base_name)[0] + ".txt"
                    output_path = os.path.join(output_dir, file_name)
                    with open(output_path, "w", encoding="utf-8") as out_file:
                        out_file.write(text.strip())

                return "Successfully extracted text from PDF." if not output_dir else f"Text extracted and saved to {output_path}"

        except FileNotFoundError:
            return f"Error: File not found at path: {file_path}"
        except Exception as e:
            return f"Error reading PDF: {str(e)}"
