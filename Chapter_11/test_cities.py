# Exercise 11-1
from city_functions import city_info

def test_city_country():
    """Test if input like 'santiago', 'chile' will work"""
    city_string = city_info('santiago', 'chile')

    assert city_string == "Santiago, Chile"

def test_city_country_population():
    """Test if input like 'santiago', 'chile', 5_000_000 will work"""
    city_string = city_info('santiago', 'chile', population=5_000_000)

    assert city_string == "Santiago, Chile - population 5000000"