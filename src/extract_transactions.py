import csv

'''
Visit https://pdftables.com/pdf-to-excel-api#python for extracting transactions from PDF to CSV format.
You need to create API Key to perform operation. Signing up https://pdftables.com/ will give you API key.
'''
def extract_transaction_from_pdf(pdf_path):
    import pdftables_api
    c = pdftables_api.Client('my-api-key')
    c.csv(pdf_path, 'pdf-transaction-analysis\dataset\Test CSV.csv')


def extract_transaction_details(csv_file):
    transactions = []

    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            app_id = row.get('App ID', '')
            xref = row.get('Xref', '')
            settlement_date = row.get('Settlement Date', '')
            broker = row.get('Broker', '')
            sub_broker = row.get('Sub Broker', '')
            borrower_name = row.get('Borrower Name', '')
            description = row.get('Description', '')
            total_loan_amount = row.get('Total Loan Amount', '')
            commission_rate = row.get('Comm Rate', '')
            upfront = row.get('Upfront', '')
            upfront_incl_gst = row.get('Upfront Incl GST', '')

            transaction = {
                'App ID': app_id,
                'Xref': xref,
                'Settlement Date': settlement_date,
                'Broker': broker,
                'Sub Broker': sub_broker,
                'Borrower Name': borrower_name,
                'Description': description,
                'Total Loan Amount': total_loan_amount,
                'Comm Rate': commission_rate,
                'Upfront': upfront,
                'Upfront Incl GST': upfront_incl_gst
            }

            transactions.append(transaction)

    return transactions