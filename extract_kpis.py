import os
import sys
import pandas as pd
import json
import re

def parse_value(raw_string):
    """
    Simulates parsing a raw string into a float, handling 'million'/'billion' and removing symbols.
    This is a simplified example of the 'Raw Extraction Separation' principle.
    """
    s = raw_string.lower().replace('$', '').replace(',', '').strip()
    multiplier = 1.0
    
    if 'billion' in s:
        multiplier = 1e9
        s = s.replace('billion', '').strip()
    elif 'million' in s:
        multiplier = 1e6
        s = s.replace('million', '').strip()
    
    try:
        return float(s) * multiplier
    except ValueError:
        return None # Return None if parsing fails, demonstrating the need for validation

def extract_kpis():
    """
    Extracts KPIs using regex and structures the output for human validation.
    """
    print("--- Running extract_kpis.py (Realistic Mock) ---")
    
    output_dir = "../output"
    sections_path = os.path.join(output_dir, "mock_report_sections.json")
    
    if not os.path.exists(sections_path):
        print(f"ERROR: Sections file not found at {sections_path}. Run identify_sections.py first.")
        sys.exit(1)

    with open(sections_path, "r") as f:
        section_data = json.load(f)

    kpi_mentions = []
    
    # Regex to find potential financial figures: $X.X million/billion, $X,XXX,XXX, or X%
    # This is a simplified regex for demonstration.
    kpi_regex = re.compile(r"(\$[\d,\.]+\s*(?:million|billion)?|\d+%)")
    
    for section in section_data["sections"]:
        page_text = section["page_text"]
        page_num = section["start_page"]
        
        # Find all matches in the page text
        for match in kpi_regex.finditer(page_text):
            raw_value_string = match.group(1).strip()
            
            # Find the surrounding context (raw_text_snippet)
            start, end = match.span()
            snippet_start = max(0, start - 50)
            snippet_end = min(len(page_text), end + 50)
            raw_text_snippet = page_text[snippet_start:snippet_end].replace('\n', ' ')
            
            # Determine KPI Name (simplified: based on surrounding text)
            kpi_name = "Financial Metric"
            if "Revenue" in raw_text_snippet:
                kpi_name = "Revenue"
            elif "Net Income" in raw_text_snippet:
                kpi_name = "Net Income (GAAP)"
            elif "EBITDA" in raw_text_snippet:
                kpi_name = "Adjusted EBITDA (Non-GAAP)"
            elif "%" in raw_value_string:
                kpi_name = "Growth Rate"
            
            # Apply the parsing logic
            parsed_value = parse_value(raw_value_string)
            
            kpi_mentions.append({
                "kpi_name": kpi_name,
                "raw_text_snippet": raw_text_snippet,
                "raw_value_string": raw_value_string,
                "parsed_value": parsed_value,
                "source_page": page_num,
                "validation_required": True, # Force validation
                "metric_type": "Non-GAAP" if "Non-GAAP" in kpi_name else "GAAP/Other"
            })

    # Save as CSV
    df = pd.DataFrame(kpi_mentions)
    csv_path = os.path.join(output_dir, "kpi_mentions.csv")
    df.to_csv(csv_path, index=False)
    print(f"SUCCESS: KPI mentions saved to {csv_path}")

    # Save as JSON
    json_path = os.path.join(output_dir, "kpi_mentions.json")
    with open(json_path, "w") as f:
        json.dump(kpi_mentions, f, indent=4)
    print(f"SUCCESS: KPI mentions saved to {json_path}")

if __name__ == "__main__":
    # Ensure pandas is installed for this script to run
    try:
        import pandas as pd
    except ImportError:
        print("ERROR: pandas library not found. Please run 'pip install pandas' first.")
        sys.exit(1)
        
    extract_kpis()
