import sys
import math
import pytest
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from app import add, sub, mul, div, log, square, sqrt, sin, cos, percent

# ADDITION TESTS

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10

def test_add_positives():
    assert add(2, 5) == 7

def test_add_negatives():
    assert add(-9,-8) == -17

def test_add_zero():
    assert add(4,0) == 4

def test_add_floats():
    assert add(3.42,5.99) == 9.41

def test_add_large_numbers():
    assert add(1e10, 1e10) == 2e10

#SUBTRACTION TESTS

def test_sub_positives():
    assert sub(5, 3) == 2

def test_sub_negative_result():
    assert sub(3, 5) == -2

def test_sub_negatives():
    assert sub(5, -3) == 8

def test_sub_zero():
    assert sub(5,0) == 5

def test_sub_floats():
    assert sub(5.5, 2.5) == 3.0

# MULTIPLICATION TESTS

def test_mul_positives():
    assert mul(3, 4) == 12
    
def test_mul_negatives():
    assert mul(-3, 4) == -12
    
def test_mul_zero():
    assert mul(5, 0) == 0
    
def test_mul_one():
    assert mul(5, 1) == 5
    
def test_mul_floats():
    assert mul(2.5, 5) == 12.5

# DIVISION TESTS

def test_div_positives():
    assert div(10, 2) == 5
    
def test_div_negatives():
    assert div(-10, 2) == -5
    
def test_div_result_float():
    assert div(10, 3) == pytest.approx(3.333333, rel=1e-5)
    
def test_div_by_one():
    assert div(5, 1) == 5
    
def test_div_zero_numerator():
    assert div(0, 5) == 0

def test_div_by_zero():
    with pytest.raises(ValueError, match="Can't divide by zero"): div(5, 0)

# TEST LOG

def test_log_natural():
    assert log(math.e) == pytest.approx(1.0)
    
def test_log_base_10():
    assert log(10, 10) == pytest.approx(1.0)
    
def test_log_base_2():
    assert log(2, 2) == pytest.approx(1.0)
    
def test_log_negative_number():
    with pytest.raises(ValueError, match="Can't calculate log of non-positive number"): log(-5)
    
def test_log_zero():
    with pytest.raises(ValueError, match="Can't calculate log of non-positive number"): log(0)
    
def test_log_invalid_base():
    with pytest.raises(ValueError, match="Base must be positive and not equal to 1"): log(10, -2)

# TEST SQUARE

def test_square_positive():
    assert square(2) == 4
    
def test_square_negative():
    assert square(-2) == 4
    
def test_square_zero():
    assert square(0) == 0
    
def test_square_float():
    assert square(2.5) == 6.25

# TEST SQUARE ROOT

def test_sqrt_positive():
    assert sqrt(4) == pytest.approx(2.0)
    
def test_sqrt_zero():
    assert sqrt(0) == pytest.approx(0.0)
    
def test_sqrt_float():
    assert sqrt(2.25) == pytest.approx(1.5)
    
def test_sqrt_large_number():
    assert sqrt(10000) == pytest.approx(100.0)
    
def test_sqrt_negative():
    with pytest.raises(ValueError, match="Cannot calculate square root of negative number"): sqrt(-4)

# TEST SIN

def test_sin_zero():
    assert sin(0) == pytest.approx(0.0)
    
def test_sin_pi():
    assert sin(math.pi) == pytest.approx(0.0, abs=1e-10)
    
def test_sin_half_pi():
    assert sin(math.pi / 2) == pytest.approx(1.0)
    
def test_sin_negative():
    assert sin(-math.pi / 2) == pytest.approx(-1.0)
    
def test_sin_common_values():
    assert sin(math.pi / 6) == pytest.approx(0.5)

# TEST COS

def test_cos_zero():
    assert cos(0) == pytest.approx(1.0)
    
def test_cos_pi():
    assert cos(math.pi) == pytest.approx(-1.0)
    
def test_cos_half_pi():
    assert cos(math.pi / 2) == pytest.approx(0.0, abs=1e-10)
    
def test_cos_negative():
    assert cos(-math.pi) == pytest.approx(-1.0)
    
def test_cos_common_values():
    assert cos(math.pi / 3) == pytest.approx(0.5)

# TEST PERCENT

def test_percentage_basic():
    assert percent(25, 100) == 25.0
    
def test_percentage_over_100():
    assert percent(150, 100) == 150.0
    
def test_percentage_zero_numerator():
    assert percent(0, 100) == 0.0
    
def test_percentage_float():
    assert percent(12.5, 50) == 25.0
    
def test_percentage_negative():
    assert percent(-25, 100) == -25.0
    
def test_percentage_zero_denominator():
    with pytest.raises(ValueError, match="Cannot calculate percentage with zero as the total"): percent(25, 0)

# TEST EDGE CASES

def test_very_small_numbers():
    small = 1e-10
    assert add(small, small) == pytest.approx(2e-10)
    
def test_very_large_numbers():
    large = 1e100
    assert add(large, large) == pytest.approx(2e100)
    
def test_mixed_types():
    assert add(5, 2.5) == 7.5
    assert mul(3, 1.5) == 4.5
    assert sub(10.5, 5) == 5.5
