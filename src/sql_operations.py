import database_utils

#Task 1: Calculate total loan amount between date range
def get_total_loan_amount_result(start_date, end_date):
    query1 = "SELECT SUM(total_loan_amount) AS total_loan_amount_of_rows FROM transactions WHERE settlement_date BETWEEN '"+ start_date +"' AND '"+ end_date +"';"
    
    total_loan_amount_result = database_utils.execute_query(query1)
    print(f"Total loan amount during 01-10-2023 to 20-10-2023: {total_loan_amount_result[0][0]}")

# Task 2: Calculate the highest loan amount given by a broker
def get_highest_loan_amount_given_by_each_broker():
    query2 = "SELECT broker, MAX(total_loan_amount) AS highest_loan_amount FROM transactions GROUP BY broker;"

    highest_loan_amount_result = database_utils.execute_query(query2)
    print("Highest loan amount given by each broker:")
    for row in highest_loan_amount_result:
        print(f"{row[0]}: {row[1]}")