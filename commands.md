# Terminal Record: Ridgeline Tool Rental

## 1. Building the project
```zsh
python3 -m venv .venv
source .venv/bin/activate
pip install pytest ruff
touch business_rules.py main.py commands.md README.md requirements.txt .gitignore
mkdir tests
touch tests/__init__.py tests/test_business_rules.py
pip freeze > requirements.txt
git init
git add .
git commit -m "initial commit"
```

## 2. The virtual environment
```zsh
which python3
```
```zsh
/home/emirc/ism3232-midterm/.venv/bin/python3
```
The presence of `.venv/bin/python3` in the output shows that the active Python interpreter is running inside the project's virtual environment.

## 3. The project structure
```zsh
tree -L 2
```
```zsh
.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```
The `.venv` folder is on my computer but not in my GitHub repository because it is excluded by `.gitignore`.

## 4. Every function and test
```zsh
rg 'def '
```
```zsh
business_rules.py
17:def calculate_rental_cost(daily_rate: float, days: int) -> float:
22:def get_rental_discount(days: int, contractor: bool = False) -> float:
37:def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
49:def requires_deposit(quote: float) -> bool:
54:def needs_inspection(days: int, quote: float) -> bool:
59:def total_quoted(rentals: list) -> float:
70:def largest_rental(rentals: list) -> str:
89:def format_rental_line(

tests/test_business_rules.py
14:def test_calculate_rental_cost():
20:def test_calculate_rental_cost_zero_days():
25:def test_get_rental_discount_fewer_than_three_days():
31:def test_get_rental_discount_three_days_limit():
37:def test_get_rental_discount_six_to_seven_days_limit():
43:def test_get_rental_discount_contractor_override():
50:def test_get_rental_discount_seven_plus_days_contractor():
55:def test_calculate_quote_damage_waiver_threshold():
61:def test_calculate_quote_high_value_with_waiver():
66:def test_requires_deposit_limit():
72:def test_requires_deposit_well_above_limit():
77:def test_needs_inspection_days_limit():
83:def test_needs_inspection_quote_limit():
89:def test_needs_inspection_neither_condition_met():
94:def test_total_quoted_with_sample_list():
103:def test_total_quoted_empty_list():
108:def test_largest_rental_standard():
117:def test_largest_rental_tie_returns_first():
126:def test_largest_rental_empty_list():
131:def test_format_rental_line():

main.py
23:def main() -> None:
```
The business_rules.py file defines 8 functions, and the tests/test_business_rules.py file defines 20 tests.

## 5. Which files print
```zsh
rg -l 'print'
```
```zsh
main.py
```
The main.py file is the only Python file that prints, and business_rules.py is not in the list because its functions return values instead of printing them directly.

## 6. The commit history
```zsh
git log --oneline
```
```zsh
a775f78 (HEAD -> main) add commands documentation
bb52ec9 add gitignore configuration
2519c74 add unit test suite with 20 tests
2174187 add main execution script and rental report
8ccc7a2 add business rules module
```
There were 5 commits at that point.