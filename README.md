# ISM3232 Midterm: Ridgeline Tool Rental

- **Name:** Emir Cihaner
- **Version:** ALPHA
- **Date:** October 25, 2026

## What This Program Does
It calculates discounts and rentals. It also provides a summary of all transactions with a report.

## Business Rules
1. Cost is daily rate times days.
2. Discounts are tiered: 0% under 3 days, 10% for 3 to 6 days, and 20% for 7+ days.
3. Licensed contractors always get at least a 10% discount.
4. A $25 damage waiver applies if the discounted cost is under $150.
5. Quotes of $1,000 or more require a deposit.
6. Rentals need an inspection if they run 5+ days and the quote exceeds $800.

## How to Run
```zsh
python3 -m venv .venv
source .venv/bin/activate
pip install pytest ruff
python main.py
```

## How to Test
```zsh
ruff format .
ruff check .
pytest -v
```
This test suite contains 20 passing unit tests.

## Files in This Repository
- `business_rules.py`: Holds the calculations.
- `main.py`: Holds the rental report.
- `commands.md`: Terminal record.
- `README.md`: Project documentation.
- `requirements.txt`: Required Python packages.
- `.gitignore`: Files ignored by git.
- `tests/__init__.py`: Test package initializer.
- `tests/test_business_rules.py`: Unit test suite with 20 tests.

## AI Use Statement
I did not use AI for this assignment.