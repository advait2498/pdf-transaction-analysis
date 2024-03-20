# pdf-transaction-analysis

An ETL operation performed on transactional data.

This project is developed in Python 3.9. To follow the steps below, make sure you have Python installed on your system.

## Steps to Run This Project

1. **Clone the Repository**
    ```
    git clone https://github.com/advait2498/pdf-transaction-analysis.git
    ```

2. **Install Dependencies**
    ```
    pip install -r requirements.txt
    ```

3. **Execute the Code**
    The executable code is located in `src/main.py`. To run this file, execute the following command:
    ```
    python src/main.py
    ```


**Note**: The `extract_transactions` file contains the `extract_transaction_from_pdf` method, which is responsible for converting PDF files to CSV format. To create the CSV file, you'll need to sign up on pdftables.com and obtain an API key. Insert this API key into the `extract_transaction_from_pdf` function.