import os
import sys
import json

def build_outputs():
    """
    Extracts raw risk factors and ensures the VALIDATION_REQUIRED.txt is present.
    """
    print("--- Running build_outputs.py (Realistic Mock) ---")
    
    output_dir = "../output"
    sections_path = os.path.join(output_dir, "mock_report_sections.json")
    
    if not os.path.exists(sections_path):
        print(f"ERROR: Sections file not found at {sections_path}. Run identify_sections.py first.")
        sys.exit(1)

    with open(sections_path, "r") as f:
        section_data = json.load(f)

    # 1. Extract Raw Risk Factors
    risk_text = ""
    risk_section_found = False
    
    for section in section_data["sections"]:
        if "Risk Factors" in section["title"]:
            risk_section_found = True
            # Extract the relevant text from the section
            # In a real scenario, we would parse the full text based on start/end pages
            # For this mock, we use the stored page text
            risk_text = section["page_text"]
            page_num = section["start_page"]
            
            # Format the output for risks_raw.txt
            risks_raw_content = f"""
# RAW RISK FACTORS - HUMAN CLASSIFICATION REQUIRED

--- Section: {section["title"]} (Page {page_num}) ---
{risk_text.strip()}
"""
            break

    if not risk_section_found:
        risks_raw_content = "# WARNING: Risk Factors section not found in the document."

    risks_path = os.path.join(output_dir, "risks_raw.txt")
    with open(risks_path, "w") as f:
        f.write(risks_raw_content.strip())
    print(f"SUCCESS: Raw risk factors saved to {risks_path}")

    # 2. Ensure VALIDATION_REQUIRED.txt is present
    validation_path = os.path.join(output_dir, "VALIDATION_REQUIRED.txt")
    if not os.path.exists(validation_path):
        print(f"WARNING: {validation_path} not found. Re-creating a placeholder.")
        with open(validation_path, "w") as f:
            f.write("# VALIDATION REQUIRED - CHECKLIST MISSING")
    
    print(f"SUCCESS: Final outputs generated. Analyst MUST review {validation_path}")

if __name__ == "__main__":
    build_outputs()
