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
| **Mock-document ingestion** | Processes the included realistic mock-report text fixture; a production PDF/OCR ingestion adapter is not included. |
| **Key-data extraction** | Identifies KPI mentions and document sections using transparent rule-based logic. |
| **Structured output** | Writes JSON, CSV and a raw risk-factor text extract for analyst review. |
| **Human validation gate** | Ships a `VALIDATION_REQUIRED.txt` reminder because extracted CIM content must be reconciled with source documents. |

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
├── identify_sections.py    # identifies sections in the mock report fixture
├── extract_kpis.py         # extracts KPI mentions into CSV and JSON
├── build_outputs.py        # writes raw risk output and validation reminder
├── mock_report_text.txt    # realistic mock-document input
├── output/                 # versioned, generated sample outputs
└── VALIDATION_REQUIRED.txt # human-review requirement
```

## Getting Started

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/gilhermanns/cim-analyser.git
   cd cim-analyser
   ```
2. The checked-in pipeline uses only the Python standard library; no third-party runtime package is required.
3. Run the complete mock-data pipeline:
   ```bash
   python identify_sections.py
   python extract_kpis.py
   python build_outputs.py
   ```

The commands generate [`output/mock_report_sections.json`](output/mock_report_sections.json), [`output/kpi_mentions.csv`](output/kpi_mentions.csv), [`output/kpi_mentions.json`](output/kpi_mentions.json), and [`output/risks_raw.txt`](output/risks_raw.txt). These are mock-data outputs that demonstrate the pipeline shape; they are not extracted from a live CIM or a real client document.

## License & Disclaimer

This project is licensed under the MIT License. It is intended as a support tool for financial analysis and should not be used as a sole basis for investment decisions. Always verify extracted data with original sources.

---

*Entwickelt mit Unterstützung von Claude Code (Anthropic).*
