def format_name(country, city, population=None):
    if population:
        return f'{country}, {city}'.title() + f' - population {population}'
    else:
        return f'{country}, {city}'.title()


formatted_name = format_name('russia', 'moscow', 150000000)
print(formatted_name)
