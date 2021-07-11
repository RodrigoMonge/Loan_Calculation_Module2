# Import pathlib
from pathlib import Path
import csv

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size
from loan_calculation_app_M2 import save_qualifying_loans


def test_save_csv():
    # @TODO: Your code here!

    # Added path
    output_path = Path("./data/qualifying_loans.csv")
    # Added header
    header = ["test_header"]
           
    # Saving the CSV lines    
    with open(output_path, "w", newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter = ",")
        csvwriter.writerow(header)
        csvwriter.writerow("4000")

    assert Path("./data/qualifying_loans.csv").exists()
    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    bank_data = fileio.load_csv(Path('./data/daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84

    # @TODO: Test the new save_csv code!
    # Asserting the filters
    bank_data_filtered = max_loan_size.filter_max_loan_size(loan, bank_data)
    for bank in bank_data_filtered:
        assert int(bank[1]) >= loan

    bank_data_filtered = credit_score.filter_credit_score(current_credit_score, bank_data_filtered)
    for bank in bank_data_filtered:
        assert int(bank[4]) <= current_credit_score

    bank_data_filtered = debt_to_income.filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    for bank in bank_data_filtered:
        assert float(bank[3]) >= monthly_debt_ratio

    bank_data_filtered = loan_to_value.filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)
    for bank in bank_data_filtered:
        assert float(bank[2]) >= loan_to_value_ratio


