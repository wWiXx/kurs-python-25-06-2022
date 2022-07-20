import logging

logging.basicConfig(level=logging.INFO, filename="kalkulator.logs")
logger = logging.getLogger(__name__)
logger.debug("Mało ważne")
logger.info("informacja")
logger.warning("Ostrzeżenie")
logger.error("Error -błąd")
logger.critical("Błąd krytyczny")


def suma(a, b):
    logger.info(f"Wywołanie suma z argumentami: {a} {b}")
    return a + b


def odejmowanie(a, b):
    logger.info(f"Wywołanie odejmowanie z argumentami: {a} {b}")
    return a - b


if __name__ == "__main__":

    def user_input():
        user_choice = int(
            input(
                "Podaj co chcesz zrobić:/"
                "1- dodawanie/"
                "2- odejmowanie/"
                "3- mnożenie/"
                "4- dzielnie"
            )
        )
        return user_choice


    def user_arguments():
        first_argument = int(input("Podaj argument a: "))
        second_argument = int(input("Podaj argument b: "))
        return first_argument, second_argument


    def operation_by_user_choice(user_choice):
        if user_choice == 1:
            x, y = user_arguments()
            return x + y


    def calculator():
        x = user_input()
        operation_by_user_choice(x)


    print(calculator())
