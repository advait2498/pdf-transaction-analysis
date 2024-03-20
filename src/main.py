import extract_transactions
import database_utils
import remove_deduplications
import generate_report
import sql_operations

CSV_FILE_PATH = r'pdf-transaction-analysis\dataset\Test PDF.csv'
PDF_FILE_PATH = r'pdf-transaction-analysis\dataset\Test PDF.pdf'

# transforming PDF file to CSV file
extract_transactions.extract_transaction_from_pdf(PDF_FILE_PATH)

# extracting list of transactions from CSV file
transactions = extract_transactions.extract_transaction_details(CSV_FILE_PATH)

# removing duplication from transaction list by considering condition of same "Xref and Total Loan Amount" in transactions
unique_transactions = remove_deduplications.remove_duplicates(transactions)

#creating SQLite3 database and transactions table
database_utils.create_database()

#performing insert operation to insert unique transactions
for transaction in transactions:
    database_utils.insert_transaction(transaction)


# Defined Start Date and End Date
start_date = '01-10-2023'
end_date =  '20-10-2023'

# User input for start date & end date. Remove comment from below code to enable user input for start date and end date. 
# start_date =  input("Enter Start Date in (DD-MM-YYYY) : ")
# end_date =  input("Enter End Date in (DD-MM-YYYY) : ")




# SQL OPERATIONS
#Task 1: Calculate total loan amount between date range
sql_operations.get_total_loan_amount_result(start_date, end_date)
# Task 2: Calculate the highest loan amount given by a broker
sql_operations.get_highest_loan_amount_given_by_each_broker()



# REPORTING

# Generate daily report summary
daily_report_summary = generate_report.generate_daily_report_summary(start_date, end_date)
print("Daily Report Summary:", daily_report_summary)

# Generate weekly report summary
weekly_report_summary = generate_report.generate_weekly_report_summary(start_date, end_date)
print("Weekly Report Summary:", weekly_report_summary)

# Generate monthly report summary
monthly_report_summary = generate_report.generate_monthly_report_summary(start_date, end_date)
print("Monthly Report Summary:", monthly_report_summary)

# Combine reports and sort loan amounts for each broker
report_summary = {}
for report in [daily_report_summary, weekly_report_summary, monthly_report_summary]:
    if report is not None:
        for row in report:
            broker = row[1]
            total_loan_amount = row[2]
            if broker not in report_summary:
                report_summary[broker] = 0
            report_summary[broker] += total_loan_amount

# Sort the report summary by loan amounts in descending order
sorted_report_summary = sorted(report_summary.items(), key=lambda x: x[1], reverse=True)

# Print the report summary
print("Broker Report Summary:")
for broker, total_loan_amount in sorted_report_summary:
    print(f"{broker}: {total_loan_amount}")


# Generate report of total loan amount grouped by date
total_loan_amount_by_date_report = generate_report.generate_total_loan_amount_by_date()

# Print the report
print("Total Loan Amount by Date Report:")
for row in total_loan_amount_by_date_report:
    print(f"{row[0]}: {row[1]}")


# Add tier_level column to the transactions table
# This operation should done first and only one time else will get sql error
# generate_report.create_tier_level_column()

# Define tier levels for each transaction
generate_report.define_tier_levels()

# Generate report of the number of loans under each tier group by date
loan_count_by_tier_and_date_report = generate_report.generate_loan_count_by_tier_and_date()

# Print the report
print("Loan Count by Tier and Date Report:")
for row in loan_count_by_tier_and_date_report:
    print(f"Date: {row[0]}, Tier Level: {row[1]}, Number of Loans: {row[2]}")