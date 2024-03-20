def remove_duplicates(transactions):
    unique_transactions = []
    seen_transactions = set()
    for transaction in transactions:
        key = (transaction['Xref'], transaction['Total Loan Amount'])
        if key not in seen_transactions:
            seen_transactions.add(key)
            unique_transactions.append(transaction)
    return unique_transactions