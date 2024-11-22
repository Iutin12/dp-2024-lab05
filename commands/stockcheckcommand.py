from typing import Any
from interface.icommand import ICommand

class StockCheckCommand(ICommand):
    """
    Команда для проверки наличия товара на складе
    """

    def __init__(self, handler: Any, order: dict) -> None:
        """
        Инициализация команды для проверки наличия товара на складе

        :param handler: Обработчик, который будет проверять наличие товара
        :param order: Данные заказа в виде словаря
        """
        self.handler = handler
        self.order = order

    def execute(self) -> None:
        """Выполняет проверку наличия товара на складе"""
        print("Выполнение команды: Проверка наличия товара на складе")
        self.handler.handle(self.order)
