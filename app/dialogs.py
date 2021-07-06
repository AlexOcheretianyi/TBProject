from dataclasses import dataclass


@dataclass(frozen=True)
class Messages:
    start_message: str = "Привет {name}. \nЧто бы найти номер введи:\n/search 1234567890"
    help_message: str = "В данный момент поиск возможен только в гугле Гугле."
    search_help: str = "Что бы воспользоватся поиском введи:\n/search 1234567890"
    unknown_message: str = "Ничего не понятною.\nПопробуй команду /help"


msg = Messages()
