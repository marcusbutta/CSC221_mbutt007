def cities(city, country, population=False):
    if population is not False:
        output = f"{city.title()}, {country.title()} - population {population}"
    else:
        output = f"{city.title()}, {country.title()}"
    return output
