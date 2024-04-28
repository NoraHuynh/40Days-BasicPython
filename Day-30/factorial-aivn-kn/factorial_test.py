import pytest
from factorial_aivn.factorial import fact
def test_fact_0():
    assert fact(0) == 1
def test_fact_1():
    assert fact(1) == 1
def test_fact_5():
    assert fact(5) == 120
def test_fact_10():
    assert fact(10) == 3628800
def test_fact_neg():
    with pytest.raises(ValueError):
        fact(-5)
    
if __name__ == "__main__":
    pytest.main()