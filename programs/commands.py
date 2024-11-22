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
