from interface.iorderhandler import IOrderHandler
from programs.exceptions import PaymentProcessingError
from typing import Dict
from handlers.basehendler import BaseOrderHandler

class PaymentProcessorHandler(BaseOrderHandler):

    MIN_PAYMENT_AMOUNT = 100
    def handle(self, order: Dict[str, any]) -> None:
        """
        Обрабатывает платеж. Если платеж недостаточен, вызывает исключение
        """
        print("Обработка платежа...")
        if order['payment'] < self.MIN_PAYMENT_AMOUNT:  # условие для ошибки (платеж недостаточен)
            raise PaymentProcessingError(f"Недостаточно средств для обработки платежа {order['payment']}")
        print(f"Платеж {order['payment']} принят.")

        self.handle_next(order)

    def set_next(self, handler: IOrderHandler) -> IOrderHandler:
        """
        Устанавливает следующий обработчик в цепочку
        """
        self.next_handler = handler
        return handler
