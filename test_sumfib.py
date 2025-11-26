import pytest
from sumfib import fibonacci_sum   

def test_fibonacci_sum():
    
    n = 5

    expected_sum = 7

    
    result = fibonacci_sum(n)

    assert result == expected_sum