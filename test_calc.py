import pytest
from calc import divide_numbers  # <-- Import the function being tested

test_cases = []

# 70 cases where integer division and float division yield the SAME result (Passing)
# e.g., 4 // 2 == 2.0 and 4 / 2 == 2.0
for i in range(1, 71):
    test_cases.append((f"pass_{i}", i * 2, 2, float(i))) 

# 30 cases where integer division triggers the bug because there is a remainder (Failing)
# e.g., 5 / 2 should be 2.5, but 5 // 2 results in 2 (Fails!)
for i in range(71, 101):
    # input 'a' is an odd number (i*2 + 1), input 'b' is 2. Expected is a float ending in .5
    test_cases.append((f"fail_{i}", (i * 2) + 1, 2, ((i * 2) + 1) / 2))

@pytest.mark.parametrize("name, a, b, expected", test_cases, ids=[t[0] for t in test_cases])
def test_bulk_operations(name, a, b, expected):
    # This now runs the actual code in calc.py!
    actual_result = divide_numbers(a, b)
    assert actual_result == expected
