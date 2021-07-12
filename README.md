# Loan Calculation Application

This is a python command-line interface application that allows users to see qualifying loans from lenders quickly and easily. The application works by that taking in a `daily_rate_sheet` of loan criteria from various loan providers, asks the user a number of questions to evaluate their loan eligibility, and then prompys the user if they want to export a CSV list of qualifying loans if there are any.

---

## Technologies

This project leverages python 3.7 with the following packages:

* [fire](https://github.com/google/python-fire) - For the command line interface, help page, and entrypoint.

* [questionary](https://github.com/tmbo/questionary) - For interactive user prompts and dialogs

* [pytest](https://docs.pytest.org/en/stable/) - For basic assertion testing of financial calculators and filters, and filio.


---

## Installation Guide

Before running the application first install the following dependencies.

```python
  pip install fire
  pip install questionary
  pip install pytest
  pip install mkdocs
```

---

## Usage

To use the loan qualifier application simply clone the repository and run the **loan_calculation_app_M2.py** with:

```python
python loan_calculation_app_M2.py
```

Upon launching the loan qualifier application you will be asked for a Path that contains the daily_rate_sheet followed by a set of question regarding loan filters.

![Loan Qualifier Prompts](Images/prompt_example.png)

Once qualifying loans are identifies, you will be asked if you want to export a list of qualifying loans and a Path for the file.

![Qualifying Loans Prompts](Images/qualifying_loans_prompts.png)

---

## Contributors

Brought to you by Rodrigo Monge.

---

## License

N/A
