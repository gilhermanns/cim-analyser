# CIM Analyser

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A tool designed for **Investment Banking (IB), Private Equity (PE), and Equity Research (ER)** analysts to automate the extraction and structuring of key information from Confidential Information Memoranda (CIMs), annual reports, and investor presentations.

## The Problem

Analysts spend a significant portion of their time manually reading through lengthy financial documents to extract critical data points (e.g., revenue, EBITDA, growth rates, management commentary, strategic initiatives). This is a time-consuming and error-prone process.

## The Solution

This system provides an automated pipeline to process these documents, identify relevant sections, and extract structured data. It allows financial professionals to:

-   **Accelerate Due Diligence**: Quickly get key financial and operational data.
-   **Improve Accuracy**: Reduce manual data entry errors.
-   **Focus on Analysis**: Spend less time on data extraction and more on strategic insights.

## Core Features

| Feature | Description |
| :--- | :--- |
| **Document Ingestion** | Processes PDF documents (CIMs, annual reports, investor presentations). |
| **Key Data Extraction** | Identifies and extracts financial figures (revenue, EBITDA, margins), growth rates, and strategic commentary. |
| **Structured Output** | Exports extracted data into analyst-friendly formats (e.g., Excel, JSON). |
| **Customizable Templates** | Adapt extraction rules for different document types or deal-specific requirements. |

## Technical Architecture

The system is built with a modular pipeline:

### 1. Document Preprocessing (`src/preprocessing/`)
Handles OCR (if needed), text extraction, and cleaning of PDF documents.

### 2. Information Extraction (`src/extraction/`)
Uses rule-based patterns and keyword matching to identify and extract specific data points and sections (e.g., "Key Financials", "Management Discussion & Analysis").

### 3. Data Structuring (`src/structuring/`)
Organizes the extracted raw text and numbers into a structured format suitable for financial modeling and analysis.

## Sample Output

Below is an example of extracted key financials from a mock annual report. This structured output can be directly fed into financial models.

```json
{
  "company_name": "GlobalTech Solutions Inc.",
  "report_year": 2025,
  "key_financials": {
    "revenue": {
      "value": 1500000000,
      "unit": "USD",
      "growth_yoy": "15%"
    },
    "ebitda": {
      "value": 300000000,
      "unit": "USD",
      "margin": "20%"
    },
    "net_income": {
      "value": 180000000,
      "unit": "USD"
    },
    "capex": {
      "value": 50000000,
      "unit": "USD"
    }
  },
  "strategic_highlights": [
    "Successful integration of acquired AI subsidiary.",
    "Expansion into new EMEA markets."
  ]
}
```

## Project Structure

```text
/cim-analyser
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
├── main.py                 # Main execution script
├── data/
│   ├── sample_report.pdf   # Sample PDF for testing
│   └── extraction_rules.yaml # Configuration for extraction patterns
└── src/
    ├── preprocessing/      # Document cleaning and text extraction
    ├── extraction/         # Information extraction logic
    └── structuring/        # Data structuring modules
```

## Getting Started

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/gilhermanns/cim-analyser.git
   cd cim-analyser
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure extraction rules in `data/extraction_rules.yaml`.
4. Run the analyser:
   ```bash
   python main.py --document data/sample_report.pdf
   ```

## License & Disclaimer

This project is licensed under the MIT License. It is intended as a support tool for financial analysis and should not be used as a sole basis for investment decisions. Always verify extracted data with original sources.

---

*Entwickelt mit Unterstützung von Claude Code (Anthropic).*
