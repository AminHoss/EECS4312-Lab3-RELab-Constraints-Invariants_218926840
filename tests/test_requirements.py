# Contains requirement-driven tests for the dispensing subsystem.
# TODO: create at least 3 test cases
from datetime import date, timedelta

import pytest
from src.dispense import DispenseEvent

def test_invalid_dosage():

    with pytest.raises(TypeError):
        DispenseEvent('A', 'vyvanse', '56mg', 5)

    with pytest.raises(ValueError):
        DispenseEvent('A', 'vyvanse', 0, 5)

def test_invalid_quantity():

    with pytest.raises(TypeError):
        DispenseEvent('A', 'vyvanse', 56, '100')

    with pytest.raises(TypeError):
        DispenseEvent('A', 'vyvanse', 56, 5.3)

    with pytest.raises(ValueError):
        DispenseEvent('A', 'vyvanse', 56, 0)

def test_exceeds_maximum_dosage():

    with pytest.raises(ValueError):
        DispenseEvent('A', 'vyvanse', 38, 2)

def test_cannot_add_same_twice_in_a_day():

    assert not DispenseEvent.invariant_holds([DispenseEvent('A', 'vyvanse', 33, 2)],
                                             DispenseEvent('A', 'vyvanse', 54, 1))

    assert DispenseEvent.invariant_holds([DispenseEvent('A', 'vyvanse', 33, 2)],
                                             DispenseEvent('A', 'vyvanse', 54, 1, date=date.today() - timedelta(days=1)))
