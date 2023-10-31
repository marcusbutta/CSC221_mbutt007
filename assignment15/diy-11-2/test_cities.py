import city_functions as cf


def test_city_country():
    city = "santiago"
    country = "chile"
    test = cf.cities(city, country)
    assert test == "Santiago, Chile"


def test_city_country_population():
    city = "santiago"
    country = "chile"
    population = 5614000
    test = cf.cities(city, country, population)
    assert test == "Santiago, Chile - population 5614000"
