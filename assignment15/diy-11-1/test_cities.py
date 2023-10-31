import city_functions as cf


def test_city_country():
    city = "santiago"
    country = "chile"
    test = cf.cities(city, country)
    assert test == "Santiago, Chile"
