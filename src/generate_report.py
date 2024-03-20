import database_utils

def generate_daily_report_summary(start_date, end_date):
    query = "SELECT date(settlement_date) AS date, broker, SUM(total_loan_amount) AS total_loan_amount FROM transactions WHERE settlement_date BETWEEN date('"+ start_date+ "') AND date('"+ end_date+ "') GROUP BY date(settlement_date), broker;"

    print("Daily Report Summary Query:", query)
    return database_utils.execute_query(query)

def generate_weekly_report_summary(start_date, end_date):
    query = "SELECT strftime('%Y-%W', settlement_date) AS week, broker, SUM(total_loan_amount) AS total_loan_amount FROM transactions WHERE settlement_date BETWEEN date('"+ start_date+ "') AND date('"+ end_date+ "') GROUP BY week, broker;"
    print("Weekly Report Summary Query:", query)
    return database_utils.execute_query(query)

def generate_monthly_report_summary(start_date, end_date):
    query = "SELECT strftime('%Y-%m', settlement_date) AS month, broker, SUM(total_loan_amount) AS total_loan_amount FROM transactions WHERE settlement_date BETWEEN date('"+ start_date+ "') AND date('"+ end_date+ "') GROUP BY month, broker;"

    print("Monthly Report Summary Query:", query)
    return database_utils.execute_query(query)

def generate_total_loan_amount_by_date():
    query = '''
    SELECT settlement_date AS date, SUM(total_loan_amount) AS total_loan_amount
    FROM transactions
    GROUP BY settlement_date
    ORDER BY settlement_date;
    '''
    return database_utils.execute_query(query)

def create_tier_level_column():
    query = '''
    ALTER TABLE transactions
    ADD COLUMN tier_level TEXT;
    '''
    database_utils.execute_query(query)

def define_tier_levels():
    query = '''
    UPDATE transactions
    SET tier_level = CASE
        WHEN total_loan_amount > 100000 THEN 'Tier 1'
        WHEN total_loan_amount > 50000 THEN 'Tier 2'
        WHEN total_loan_amount > 10000 THEN 'Tier 3'
        ELSE 'Tier 4'
    END;
    '''
    database_utils.execute_query(query)

def generate_loan_count_by_tier_and_date():
    query = '''
    SELECT settlement_date AS date, tier_level, COUNT(*) AS number_of_loans
    FROM transactions
    GROUP BY date, tier_level
    ORDER BY date, tier_level;
    '''
    return database_utils.execute_query(query)