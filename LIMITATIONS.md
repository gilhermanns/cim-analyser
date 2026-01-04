# CIM Analyzer: Limitations & Professional Boundaries

This system is designed to accelerate the review of Confidential Information Memorandums (CIMs) and financial reports. It is a support tool for investment professionals, not a replacement for manual diligence.

## 1. Extraction Accuracy
- **Table Complexity**: Highly non-standard tables (e.g., multi-line headers, nested rows) may result in parsing errors. All extracted KPIs must be reconciled against the source PDF.
- **OCR Quality**: The system's performance is dependent on the quality of the underlying PDF text layer. Scanned documents without high-quality OCR will result in degraded extraction.

## 2. Contextual Interpretation
- **GAAP vs. Non-GAAP**: The system identifies mentions of financial metrics but does not automatically reconcile non-GAAP adjustments. The analyst must determine the validity of "Adjusted" figures.
- **Forward-Looking Statements**: While the system flags risk factors, it does not assess the probability or impact of these risks. This remains the sole domain of the investment professional.

## 3. Scope Boundaries
- **Financial Institutions**: This tool is optimized for industrial, tech, and consumer companies. It is not designed to parse the complex balance sheets of banks or insurance companies.
- **Legal Nuance**: The NLP engine detects keywords and patterns but does not understand the legal implications of specific contract language or litigation disclosures.

## 4. Mandatory Validation
- The system generates a `VALIDATION_REQUIRED.txt` file for every run. **No data from this tool should be used in a financial model or investment committee memo without being checked off in this list.**

---
*Disclaimer: This tool is for professional research use only.*
