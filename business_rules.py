
MIN_DAYS_TIER_1 = 3
MIN_DAYS_TIER_2 = 7
TIER_1_DISCOUNT = 0.10
TIER_2_DISCOUNT = 0.20
CONTRACTOR_MIN_DISCOUNT = 0.10

DAMAGE_WAIVER_FEE = 25.00
DAMAGE_WAIVER_THRESHOLD = 150.00

DEPOSIT_THRESHOLD = 1000.00

INSPECTION_MIN_DAYS = 5
INSPECTION_QUOTE_THRESHOLD = 800.00


def calculate_rental_cost(daily_rate: float, days: int) -> float:
    """Return the rental cost before any discount."""
    return daily_rate * days


def get_rental_discount(days: int, contractor: bool = False) -> float:
    """Return the discount rate as a decimal based on days and contractor status."""
    if days >= MIN_DAYS_TIER_2:
        discount = TIER_2_DISCOUNT
    elif days >= MIN_DAYS_TIER_1:
        discount = TIER_1_DISCOUNT
    else:
        discount = 0.0

    if contractor and discount < CONTRACTOR_MIN_DISCOUNT:
        discount = CONTRACTOR_MIN_DISCOUNT

    return discount


def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
    """Return the quote for one rental including discount and damage waiver."""
    base_cost = calculate_rental_cost(daily_rate, days)
    discount_rate = get_rental_discount(days, contractor)
    discounted_cost = base_cost * (1.0 - discount_rate)

    if discounted_cost < DAMAGE_WAIVER_THRESHOLD:
        discounted_cost += DAMAGE_WAIVER_FEE

    return round(discounted_cost, 2)


def requires_deposit(quote: float) -> bool:
    """Return True when the quote requires a deposit, otherwise False."""
    return quote >= DEPOSIT_THRESHOLD


def needs_inspection(days: int, quote: float) -> bool:
    """Return True when the rental needs a pickup inspection, otherwise False."""
    return days >= INSPECTION_MIN_DAYS and quote > INSPECTION_QUOTE_THRESHOLD


def total_quoted(rentals: list) -> float:
    """Return the sum of the quotes for every rental in the list using a for loop."""
    total = 0.0
    for rental in rentals:
        quote = calculate_quote(
            rental["daily_rate"], rental["days"], rental["contractor"]
        )
        total += quote
    return round(total, 2)


def largest_rental(rentals: list) -> str:
    """Return the customer of the rental with the largest quote using a for loop."""
    if not rentals:
        return ""

    max_quote = -1.0
    largest_customer = ""

    for rental in rentals:
        quote = calculate_quote(
            rental["daily_rate"], rental["days"], rental["contractor"]
        )
        if quote > max_quote:
            max_quote = quote
            largest_customer = rental["customer"]

    return largest_customer


def format_rental_line(
    customer: str, quote: float, deposit: bool, inspection: bool
) -> str:
    """Return one formatted line of the report."""
    deposit_str = "yes" if deposit else "no"
    inspection_str = "yes" if inspection else "no"
    return f"{customer}: ${quote:.2f} | deposit: {deposit_str} | inspection: {inspection_str}"