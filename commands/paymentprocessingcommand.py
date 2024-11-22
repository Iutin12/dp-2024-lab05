from typing import Any
from interface.icommand import ICommand

class PaymentProcessingCommand(ICommand):
    """
    Команда для обработки платежа
    """

    def __init__(self, handler: Any, order: dict) -> None:
        """
        Инициализация команды для обработки платежа.

        :param handler: Обработчик, который будет обрабатывать платеж
        :param order: Данные заказа в виде словаря
        """
        self.handler = handler
        self.order = order

    def execute(self) -> None:
        """Выполняет обработку платежа"""
        print("Выполнение команды: Обработка платежа")
        self.handler.handle(self.order)

