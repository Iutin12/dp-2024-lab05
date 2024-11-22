from programs.handlers import OrderHandler, StockCheckHandler, PaymentProcessorHandler, DeliveryHandler
from programs.commands import OrderProcessingCommand
from programs.exceptions import OutOfStockError, PaymentProcessingError, DeliveryError

order: dict = {
    'item': 'item1',
    'payment': 100,
    'address': 'UGATU'
}


def main() -> None:
    """
    Основная функция для обработки заказа через цепочку обработчиков
    """
    order_handler = OrderHandler()
    stock_check_handler = StockCheckHandler()
    payment_processor_handler = PaymentProcessorHandler()
    delivery_handler = DeliveryHandler()

    order_handler.set_next(stock_check_handler).set_next(payment_processor_handler).set_next(delivery_handler)

    try:
        order_command = OrderProcessingCommand(order_handler, order)
        order_command.execute()

    except (OutOfStockError, PaymentProcessingError, DeliveryError, ValueError) as e:
        print(f"Ошибка при обработке заказа: {e}")


if __name__ == "__main__":
    main()
