from pytest import mark


ddt = {
    "argnames": "name, header, footer",
    "argvalues": [
        ("Name", "Header", "Footer"),
        ("empty_header_&_footer", "", ""),
        ("", "", ""),
        ("", "empty_name", "empty_name"),
        ("123", "", "empty_header"),
    ],
    "ids": [
        "Основной тест.",
        "Не заполнены хэдер и футер.",
        "Не заполнены все элементы.",
        "Не заполнено имя.",
        "Цифровое имя и не заполнен хэдер.",
    ],
}


@mark.parametrize(**ddt)
def test_add_group(desktop_app_auth, name, header, footer) -> None:
    desktop_app_auth.group.create(name, header, footer)


@mark.parametrize(**ddt)
def test_add_group_on_phone(mobile_app_auth, name, header, footer) -> None:
    mobile_app_auth.group.create(name, header, footer)
