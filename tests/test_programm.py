import unittest
from programs.handlers import OrderHandler, StockCheckHandler, PaymentProcessorHandler, DeliveryHandler
from programs.commands import OrderProcessingCommand, StockCheckCommand, PaymentProcessingCommand, DeliveryCommand
from programs.exceptions import OutOfStockError, PaymentProcessingError

class TestOrderProcessing(unittest.TestCase):
    """
    Тесты для обработки заказа. Проверяют успешную обработку, ошибки при отсутствии товара на складе
    и при недостаточности средств для платежа.
    """

    def setUp(self) -> None:
        """
        Настройка тестов. Создает экземпляры обработчиков и связывает их в цепочку.

        :return: None
        """
        self.order_handler = OrderHandler()
        self.stock_check_handler = StockCheckHandler()
        self.payment_processor_handler = PaymentProcessorHandler()
        self.delivery_handler = DeliveryHandler()

        # Устанавливаем цепочку обработчиков
        self.order_handler.set_next(self.stock_check_handler).set_next(self.payment_processor_handler).set_next(self.delivery_handler)

    def test_order_successful(self) -> None:
        """
        Тестирует успешную обработку заказа, включая все этапы: проверка наличия товара, обработка платежа
        и доставка.

        :return: None
        """
        order = {
            'item': 'item1',
            'payment': 100,
            'address': 'UGATU'
        }
        try:
            # Проверка каждого шага обработки заказа с использованием команд
            order_command = OrderProcessingCommand(self.order_handler, order)
            order_command.execute()

            stock_check_command = StockCheckCommand(self.stock_check_handler, order)
            stock_check_command.execute()

            payment_command = PaymentProcessingCommand(self.payment_processor_handler, order)
            payment_command.execute()

            delivery_command = DeliveryCommand(self.delivery_handler, order)
            delivery_command.execute()

            print("Заказ успешно обработан!")
        except Exception as e:
            self.fail(f"Тест не должен был вызвать исключение: {e}")

    def test_out_of_stock(self) -> None:
        """
        Тестирует ситуацию, когда товар отсутствует на складе. Ожидается исключение `OutOfStockError`.

        :return: None
        """
        order = {
            'item': 'item2',  # Товар отсутствует на складе
            'payment': 100,
            'address': 'UGATU'
        }
        with self.assertRaises(OutOfStockError):
            # Проверка наличия товара
            stock_check_command = StockCheckCommand(self.stock_check_handler, order)
            stock_check_command.execute()

    def test_insufficient_payment(self) -> None:
        """
        Тестирует ситуацию, когда платеж недостаточен для обработки заказа. Ожидается исключение `PaymentProcessingError`.

        :return: None
        """
        order = {
            'item': 'item1',
            'payment': 50,  # Платеж меньше 100
            'address': 'UGATU'
        }
        with self.assertRaises(PaymentProcessingError):
            # Обработка платежа
            payment_command = PaymentProcessingCommand(self.payment_processor_handler, order)
            payment_command.execute()


if __name__ == '__main__':
    unittest.main()
