import calculator

import pytest

# ADD
@pytest.mark.parametrize("x, y, expected_result", [
    # Test case 1: Lower boundary values
    (0, 0, 0),  # Smallest possible values for x and y
    
    # Test case 2: Typical/normal values
    (5, 10, 15),  # x and y with typical positive values
    
    # Test case 3: Upper boundary values
    (9999, 9999, 19998),  # Largest possible values for x and y
    
    # Test case 4: Testing the effect of one operand being zero
    (0, 100, 100),  # x is zero
    
    # Test case 5: Testing negative numbers
    (-5, 8, 3),  # x and y are negative numbers
    
    # Test case 6: Testing decimal numbers
    (1.5, 2.5, 4),  # x and y are decimal numbers

])

def test_add(x, y, expected_result):
    assert calculator.add(x, y) == expected_result


# SUBTRACT
@pytest.mark.parametrize("x, y, expected_result", [
    # Test case 1: Lower boundary values
    (0, 0, 0),  # Smallest possible values for x and y
    
    # Test case 2: Typical/normal values
    (5, 10, -5),  # x and y with typical positive values
    
    # Test case 3: Upper boundary values
    (9999, 9998, 1),  # Largest possible values for x and y
    
    # Test case 4: Testing the effect of one operand being zero
    (0, 100, -100),  # x is zero
    
    # Test case 5: Testing negative numbers
    (-5, 8, -13),  # x or y are negative numbers
    
    # Test case 6: Testing decimal numbers
    (1.5, 2.5, -1),  # x and y are decimal numbers

])

def test_subtract(x, y, expected_result):
    assert calculator.subtract(x, y) == expected_result


# MULTIPLY
@pytest.mark.parametrize("x, y, expected_result", [
    # Test case 1: Lower boundary values
    (0, 0, 0),  # Smallest possible values for x and y
    
    # Test case 2: Typical/normal values
    (5, 10, 50),  # x and y with typical positive values
    
    # Test case 3: Upper boundary values
    (9999, 9998, 99970002),  # Largest possible values for x and y
    
    # Test case 4: Testing the effect of one operand being zero
    (0, 100, 0),  # x is zero
    
    # Test case 5: Testing negative numbers
    (-5, 8, -40),  # x or y are negative numbers
    
    # Test case 6: Testing decimal numbers
    (1.5, 2.5, 3.75),  # x and y are decimal numbers

])

def test_multiply(x, y, expected_result):
    assert calculator.multiply(x, y) == expected_result



# DIVIDE
@pytest.mark.parametrize("x, y, expected_result", [
    # Test case 1: Lower boundary values
    (0, 0.01, 0),  # Smallest possible values for x and y
    
    # Test case 2: Typical/normal values
    (5, 10, 0.5),  # x and y with typical positive values
    
    # Test case 3: Upper boundary values
    (9999, 9999, 1),  # Largest possible values for x and y
    
    # Test case 4: Testing the effect of one operand being zero
    (0, 100, 0),  # x is zero

    # Test case 5: Testing negative numbers
    (-5, 8, -0.625),  # x and y are negative numbers
    
    # Test case 6: Testing decimal numbers
    (1.5, 2.5, 0.6),  # x and y are decimal numbers

    # Test case for zero division : Testing the effect of dividing by zero
    (100, 0, ZeroDivisionError),  # y is zero

])

def test_divide(x, y, expected_result):
    if expected_result == ZeroDivisionError:
        with pytest.raises(ZeroDivisionError):
            calculator.divide(x, y)
    else:
        assert calculator.divide(x, y) == expected_result