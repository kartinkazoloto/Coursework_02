import pycountry


def validate_country(country_name: str) -> tuple[bool, str]:
    """Проверяет существование страны и возвращает результат + сообщение"""
    if not country_name:
        # print("Пустое название")
        return False
    clear_country = country_name.strip().title()
    search_country = pycountry.countries.get(name=clear_country)

    return True

