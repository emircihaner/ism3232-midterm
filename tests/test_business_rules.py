from business_rules import (
    calculate_quote,
    calculate_rental_cost,
    format_rental_line,
    get_rental_discount,
    largest_rental,
    needs_inspection,
    requires_deposit,
    total_quoted,
)


def test_calculate_rental_cost():
    """Test standard rental cost calculation before discount."""
    assert calculate_rental_cost(50.0, 3) == 150.0
    assert calculate_rental_cost(100.0, 1) == 100.0


def test_calculate_rental_cost_zero_days():
    """Test rental cost with zero days."""
    assert calculate_rental_cost(50.0, 0) == 0.0


def test_get_rental_discount_fewer_than_three_days():
    """Test discount for rentals under 3 days without contractor status."""
    assert get_rental_discount(2, False) == 0.0
    assert get_rental_discount(1, False) == 0.0


def test_get_rental_discount_three_days_limit():
    """Test discount limits at exactly 2 and 3 days."""
    assert get_rental_discount(2, False) == 0.0
    assert get_rental_discount(3, False) == 0.10


def test_get_rental_discount_six_to_seven_days_limit():
    """Test discount limits between 6 and 7 days."""
    assert get_rental_discount(6, False) == 0.10
    assert get_rental_discount(7, False) == 0.20


def test_get_rental_discount_contractor_override():
    """Test that licensed contractors get at least 10% even under 3 days."""
    assert get_rental_discount(2, True) == 0.10
    assert get_rental_discount(5, True) == 0.10
    assert get_rental_discount(7, True) == 0.20


def test_get_rental_discount_seven_plus_days_contractor():
    """Test 20% discount for contractor renting 7+ days."""
    assert get_rental_discount(8, True) == 0.20


def test_calculate_quote_damage_waiver_threshold():
    """Test damage waiver application right below and at/above the $150 threshold."""
    assert calculate_quote(70.0, 2, False) == 165.0
    assert calculate_quote(75.0, 2, False) == 150.0


def test_calculate_quote_high_value_with_waiver():
    """Test higher quote calculation including damage waiver."""
    assert calculate_quote(100.0, 1, False) == 125.0


def test_requires_deposit_limit():
    """Test deposit requirement around the $1,000 threshold."""
    assert requires_deposit(999.99) is False
    assert requires_deposit(1000.0) is True


def test_requires_deposit_well_above_limit():
    """Test deposit requirement well above $1,000."""
    assert requires_deposit(1500.0) is True


def test_needs_inspection_days_limit():
    """Test inspection requirement around the 5-day limit with high quote."""
    assert needs_inspection(4, 900.0) is False
    assert needs_inspection(5, 900.0) is True


def test_needs_inspection_quote_limit():
    """Test inspection requirement around the $800 quote limit with high days."""
    assert needs_inspection(6, 800.0) is False
    assert needs_inspection(6, 801.0) is True


def test_needs_inspection_neither_condition_met():
    """Test inspection false when neither condition is met."""
    assert needs_inspection(3, 500.0) is False


def test_total_quoted_with_sample_list():
    """Test total_quoted sums quotes correctly across a small list."""
    sample = [
        {"customer": "Alice", "daily_rate": 50.0, "days": 2, "contractor": False},
        {"customer": "Bob", "daily_rate": 100.0, "days": 5, "contractor": False},
    ]
    assert total_quoted(sample) == 575.0


def test_total_quoted_empty_list():
    """Test total_quoted with empty list returns zero."""
    assert total_quoted([]) == 0.0


def test_largest_rental_standard():
    """Test largest_rental identifies the correct customer."""
    sample = [
        {"customer": "Alice", "daily_rate": 50.0, "days": 2, "contractor": False},
        {"customer": "Bob", "daily_rate": 200.0, "days": 10, "contractor": False},
    ]
    assert largest_rental(sample) == "Bob"


def test_largest_rental_tie_returns_first():
    """Test largest_rental returns the first customer in case of a tie."""
    sample = [
        {"customer": "Alice", "daily_rate": 100.0, "days": 5, "contractor": False},
        {"customer": "Bob", "daily_rate": 100.0, "days": 5, "contractor": False},
    ]
    assert largest_rental(sample) == "Alice"


def test_largest_rental_empty_list():
    """Test largest_rental returns an empty string for an empty list."""
    assert largest_rental([]) == ""


def test_format_rental_line():
    """Test format_rental_line returns the expected string format."""
    result = format_rental_line("Alvarez", 145.0, False, False)
    assert result == "Alvarez: $145.00 | deposit: no | inspection: no"
