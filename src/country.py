import pycountry


def validate_country(country_name: str) -> bool:
    """Проверяет существование страны и возвращает результат"""
    if not country_name:
        # print("Пустое название")
        return False
    clear_country = country_name.strip().title()
    search_country = pycountry.countries.get(name=clear_country)
    # if search_country == clear_country:
    return True
