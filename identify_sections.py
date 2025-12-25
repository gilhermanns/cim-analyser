import os
import json
import sys
import re

def identify_sections():
    """
    Identifies key sections from the raw text using regex and calculates page ranges.
    """
    print("--- Running identify_sections.py (Realistic Mock) ---")
    
    processed_dir = "../data/processed"
    output_dir = "../output"
    
    input_path = os.path.join(processed_dir, "mock_report_text.txt")
    output_path = os.path.join(output_dir, "mock_report_sections.json")
    
    if not os.path.exists(input_path):
        print(f"ERROR: Input file not found at {input_path}. Run extract_text.py first.")
        sys.exit(1)

    with open(input_path, "r") as f:
        full_text = f.read()

    # Split text by the page break marker
    pages = full_text.split("\n\n--- PAGE BREAK ---\n\n")
    
    section_data = {
        "report_name": "mock_report",
        "sections": []
    }
    
    # Regex to find section headers (e.g., "Page X: Section Name")
    section_regex = re.compile(r"Page \d+: (.*)")
    
    for i, page_text in enumerate(pages):
        page_num = i + 1
        match = section_regex.search(page_text)
        
        if match:
            title = match.group(1).strip()
            
            # Simple logic: section starts on this page and ends on the page before the next section
            # or at the end of the document.
            
            # For this mock, we'll just record the start page and a snippet
            section_data["sections"].append({
                "title": title,
                "start_page": page_num,
                "text_snippet": page_text[:100].replace('\n', ' ') + "...",
                "page_text": page_text # Store full page text for downstream processing
            })
    
    try:
        with open(output_path, "w") as f:
            json.dump(section_data, f, indent=4)
        
        print(f"SUCCESS: Identified sections and saved to {output_path}")
        
    except Exception as e:
        print(f"ERROR: Failed to write section data: {e}")
        sys.exit(1)

if __name__ == "__main__":
    identify_sections()
