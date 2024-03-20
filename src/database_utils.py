import sqlite3

def create_database():
    try:
        conn = sqlite3.connect('transactions.db')
        cursor = conn.cursor()

        # Create a table to store transaction details
        cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                            id INTEGER PRIMARY KEY,
                            app_id TEXT,
                            xref TEXT,
                            settlement_date TEXT,
                            broker TEXT,
                            sub_broker TEXT,
                            borrower_name TEXT,
                            description TEXT,
                            total_loan_amount REAL,
                            commission_rate REAL,
                            upfront REAL,
                            upfront_incl_gst REAL
                        )''')

        conn.commit()
        conn.close()
    except sqlite3.Error as err:
        raise err

def insert_transaction(transaction):
    try:
        conn = sqlite3.connect('transactions.db')
        c = conn.cursor()
        c.execute('''INSERT INTO transactions (
                        app_id, xref, settlement_date, broker, sub_broker,
                        borrower_name, description, total_loan_amount,
                        commission_rate, upfront, upfront_incl_gst
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (transaction['App ID'], transaction['Xref'], transaction['Settlement Date'],
                transaction['Broker'], transaction['Sub Broker'], transaction['Borrower Name'],
                transaction['Description'], transaction['Total Loan Amount'],
                transaction['Comm Rate'], transaction['Upfront'], transaction['Upfront Incl GST']))
        conn.commit()
        conn.close()
    except sqlite3.Error as err:
        raise err

def execute_query(query):
    try:
        conn = sqlite3.connect('transactions.db')
        c = conn.cursor()
        c.execute(query)
        result = c.fetchall()
        conn.close()
        return result
    except sqlite3.DataError as err:
        raise err