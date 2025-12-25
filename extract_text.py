"""
Extract text from PDF documents page by page.
Maintains full traceability to source pages.
"""

import pdfplumber
from pathlib import Path


def extract_pdf_text(pdf_path):
    """
    Extract text from a PDF file, page by page.
    
    Args:
        pdf_path: Path to PDF file
        
    Returns:
        str: Full text with page delimiters
    """
    text_parts = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, start=1):
            page_text = page.extract_text()
            
            if page_text:
                text_parts.append(f"--- PAGE {i} ---")
                text_parts.append(page_text)
                text_parts.append("")  # blank line between pages
    
    return "\n".join(text_parts)


def process_all_pdfs(raw_dir, processed_dir):
    """
    Process all PDFs in raw directory and save to processed directory.
    
    Args:
        raw_dir: Directory containing raw PDF files
        processed_dir: Directory to save processed text files
    """
    raw_path = Path(raw_dir)
    processed_path = Path(processed_dir)
    
    # Create processed directory if it doesn't exist
    processed_path.mkdir(parents=True, exist_ok=True)
    
    # Process each PDF
    pdf_files = list(raw_path.glob("*.pdf"))
    
    if not pdf_files:
        print(f"No PDF files found in {raw_dir}")
        return
    
    for pdf_file in pdf_files:
        print(f"Processing: {pdf_file.name}")
        
        try:
            text = extract_pdf_text(pdf_file)
            
            # Save with same name but .txt extension
            output_file = processed_path / f"{pdf_file.stem}.txt"
            output_file.write_text(text, encoding='utf-8')
            
            print(f"  Saved to: {output_file.name}")
            
        except Exception as e:
            print(f"  ERROR processing {pdf_file.name}: {e}")


if __name__ == "__main__":
    # Run extraction
    process_all_pdfs("data/raw", "data/processed")
    print("\nText extraction complete.")