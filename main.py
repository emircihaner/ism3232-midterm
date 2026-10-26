
from business_rules import (
    calculate_quote,
    requires_deposit,
    needs_inspection,
    total_quoted,
    largest_rental,
    format_rental_line,
)

rentals = [
    {"customer": "Alvarez", "daily_rate": 60.00, "days": 2, "contractor": False},
    {"customer": "Brennan", "daily_rate": 60.00, "days": 2, "contractor": True},
    {"customer": "Chowdhury", "daily_rate": 85.00, "days": 4, "contractor": False},
    {"customer": "Dvorak", "daily_rate": 120.00, "days": 10, "contractor": False},
    {"customer": "Eastman", "daily_rate": 210.00, "days": 8, "contractor": True},
    {"customer": "Fujita", "daily_rate": 250.00, "days": 4, "contractor": False},
    {"customer": "Garza", "daily_rate": 95.00, "days": 5, "contractor": True},
    {"customer": "Hughes", "daily_rate": 200.00, "days": 7, "contractor": False},
]


def main() -> None:
    """Run the rental report and print results."""
    print("Ridgeline Tool Rental - Rental Report")

    rental_count = 0
    deposit_count = 0
    inspection_count = 0

    for rental in rentals:
        rental_count += 1
        customer = rental["customer"]
        rate = rental["daily_rate"]
        days = rental["days"]
        contractor = rental["contractor"]

        quote = calculate_quote(rate, days, contractor)
        deposit = requires_deposit(quote)
        inspection = needs_inspection(days, quote)

        if deposit:
            deposit_count += 1
        if inspection:
            inspection_count += 1

        line = format_rental_line(customer, quote, deposit, inspection)
        print(line)

    total = total_quoted(rentals)
    average = total / rental_count if rental_count > 0 else 0.0
    largest = largest_rental(rentals)

    print(f"Rentals: {rental_count}")
    print(f"Total quoted: ${total:.2f}")
    print(f"Average quote: ${average:.2f}")
    print(f"Largest quote: {largest}")
    print(f"Deposits required: {deposit_count}")
    print(f"Inspections required: {inspection_count}")


if __name__ == "__main__":
    main()