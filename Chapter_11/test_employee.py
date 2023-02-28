# Exercise 11-3
import pytest
from employee_class import Employee

@pytest.fixture
def my_employee():
    """An employee instance that will be available to all test functions"""
    my_employee = Employee('pete', 'jordan', 50_000)
    return my_employee


def test_give_default_raise(my_employee):
    """Test to make sure a default raise works"""
    my_employee.give_raise()

    assert my_employee.first_name == 'Pete'
    assert my_employee.last_name == 'Jordan'
    assert my_employee.salary == 55000


def test_give_custom_raise(my_employee):
    """Test to make sure a custom raise works"""
    my_employee.give_raise(10_000)

    assert my_employee.first_name == 'Pete'
    assert my_employee.last_name == 'Jordan'
    assert my_employee.salary == 60000