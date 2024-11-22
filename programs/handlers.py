from interface.iorderhandler import IOrderHandler
from programs.exceptions import OutOfStockError, PaymentProcessingError, DeliveryError
from programs.inventory import inventory
from typing import Dict, Optional

class StockCheckHandler(IOrderHandler):
    def __init__(self):
        self.next_handler: Optional[IOrderHandler] = None

    def handle(self, order: Dict[str, any]) -> None:
        """
        Проверяет наличие товара на складе. Если товар отсутствует, вызывает исключение
        """
        print("Проверка наличия товара на складе...")
        if inventory.get(order['item'], 0) <= 0:
            raise OutOfStockError(f"Товар {order['item']} отсутствует на складе")
        print(f"Товар {order['item']} в наличии.")

        if self.next_handler:
            self.next_handler.handle(order)

    def set_next(self, handler: IOrderHandler) -> IOrderHandler:
        """
        Устанавливает следующий обработчик в цепочку.
        """
        self.next_handler = handler
        return handler


class PaymentProcessorHandler(IOrderHandler):
    def __init__(self):
        self.next_handler: Optional[IOrderHandler] = None

    def handle(self, order: Dict[str, any]) -> None:
        """
        Обрабатывает платеж. Если платеж недостаточен, вызывает исключение.
        """
        print("Обработка платежа...")
        if order['payment'] < 100:  # условие для ошибки (платеж недостаточен)
            raise PaymentProcessingError(f"Недостаточно средств для обработки платежа {order['payment']}")
        print(f"Платеж {order['payment']} принят.")

        if self.next_handler:
            self.next_handler.handle(order)

    def set_next(self, handler: IOrderHandler) -> IOrderHandler:
        """
        Устанавливает следующий обработчик в цепочку
        """
        self.next_handler = handler
        return handler


class DeliveryHandler(IOrderHandler):
    def __init__(self):
        self.next_handler: Optional[IOrderHandler] = None

    def handle(self, order: Dict[str, any]) -> None:
        """
        Осуществляет доставку товара. Если адрес не указан, вызывает исключение.
        """
        print(f"Доставка товара на адрес {order['address']}...")
        if not order['address']:
            raise DeliveryError("Адрес доставки не указан.")
        print(f"Заказ доставлен по адресу {order['address']}.")

    def set_next(self, handler: IOrderHandler) -> IOrderHandler:
        """
        Устанавливает следующий обработчик в цепочку.
        """
        self.next_handler = handler
        return handler


class OrderHandler(IOrderHandler):
    def __init__(self):
        self.next_handler: Optional[IOrderHandler] = None

    def handle(self, order: Dict[str, any]) -> None:
        """
        Выполняет начальную обработку заказа. Проверяет наличие всех обязательных данных
        """
        print("Начальная обработка заказа...")
        if 'item' not in order or 'payment' not in order or 'address' not in order:
            raise ValueError("Не все данные заказа предоставлены.")

        if self.next_handler:
            self.next_handler.handle(order)

    def set_next(self, handler: IOrderHandler) -> IOrderHandler:
        """
        Устанавливает следующий обработчик в цепочку
        """
        self.next_handler = handler
        return handler
