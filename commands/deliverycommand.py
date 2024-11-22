from typing import Any
from interface.icommand import ICommand

class DeliveryCommand(ICommand):
    """
    Команда для доставки товара
    """

    def __init__(self, handler: Any, order: dict) -> None:
        """
        Инициализация команды для доставки товара

        :param handler: Обработчик, который будет осуществлять доставку
        :param order: Данные заказа в виде словаря
        """
        self.handler = handler
        self.order = order

    def execute(self) -> None:
        """Выполняет доставку товара"""
        print("Выполнение команды: Доставка товара")
        self.handler.handle(self.order)
