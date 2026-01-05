# 📄 CIM & Financial Report Analyzer

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![IB-Grade](https://img.shields.io/badge/Industry-Investment%20Banking-blue.svg)]()

An automated extraction and analysis pipeline for **Confidential Information Memorandums (CIMs)**, Annual Reports, and Investor Presentations. This tool accelerates the "first-read" phase for Investment Banking and Private Equity analysts by automatically identifying key financial sections and extracting critical KPIs.

---

## 💡 Core Value Proposition

Reviewing a 100-page CIM or Annual Report is time-consuming. This tool provides a "Human-in-the-loop" automation framework to:

| Feature | Benefit |
| :--- | :--- |
| **Automated Sectioning** | Instantly identifies "Risk Factors", "Financial Highlights", and "Management Discussion". |
| **KPI Extraction** | Pulls EBITDA, Revenue, and Margin figures directly from the text. |
| **Audit Trail** | Links every extracted value to its source page and context for easy verification. |
| **Validation Workflow** | Generates a mandatory checklist to ensure 100% accuracy before modeling. |

---

## 🛠 Technical Architecture

### 1. Extraction Layer (`extract_text.py`)
Uses `pdfplumber` for high-fidelity text extraction, preserving the spatial relationship of financial figures.

### 2. Intelligence Layer (`identify_sections.py` & `extract_kpis.py`)
*   **Sectioning**: Uses keyword-density and structural markers to map the document's architecture.
*   **KPI Engine**: Employs proximity-based search to link financial labels (e.g., "Adj. EBITDA") with their corresponding numerical values.

### 3. Audit Layer (`build_outputs.py`)
Ensures that the automation is auditable. It generates a raw risk factor summary and a validation checklist that must be reviewed by a human analyst.

---

## 📊 Project Structure

```text
/cim-analyser
├── README.md               # Comprehensive project documentation
├── LIMITATIONS.md          # Mature disclosure of system boundaries
├── extract_text.py         # PDF text extraction engine
├── identify_sections.py    # Document architecture mapping
├── extract_kpis.py         # Financial metric extraction
├── build_outputs.py        # Audit trail and report generation
├── data/
│   ├── raw/                # Input PDFs (CIMs, Reports)
│   └── processed/          # Intermediate text representations
└── output/                 # Extracted KPIs and Validation checklists
```

---

## 🚦 Getting Started

### Prerequisites
*   Python 3.8+
*   `pdfplumber`, `pandas`

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

### Running the Analysis
1. Place your PDF in `data/raw/`.
2. Run the pipeline:
   ```bash
   python3 extract_text.py
   python3 identify_sections.py
   python3 extract_kpis.py
   python3 build_outputs.py
   ```

---

## 🛡 License & Disclaimer

This project is licensed under the MIT License. It is a productivity tool for analysts and does not replace the need for a thorough manual review of legal and financial documents.
