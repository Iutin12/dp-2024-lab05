from typing import Any
from interface.icommand import ICommand

class OrderProcessingCommand(ICommand):
    """
    Команда для начальной обработки заказа
    """

    def __init__(self, handler: Any, order: dict) -> None:
        """
        Инициализация команды для начальной обработки заказа

        :param handler: Обработчик, который будет выполнять обработку заказа
        :param order: Данные заказа в виде словаря
        """
        self.handler = handler
        self.order = order

    def execute(self) -> None:
        """Выполняет начальную обработку заказа"""
        print("Выполнение команды: Начальная обработка заказа")
        self.handler.handle(self.order)
