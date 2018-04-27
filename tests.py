import unittest
from simsat import Wallet, Engine

class TestWallet(unittest.TestCase):
    def setUp(self):
        self.wallet = Wallet(100)

    def test_default_money(self):
        self.assertEqual(100, self.wallet.money)

    def test_increase_money(self):
        self.wallet.modify_money(10)
        self.assertEqual(110, self.wallet.money)

    def test_decrease_money(self):
        self.wallet.modify_money(-30)
        self.assertEqual(70, self.wallet.money)

    def test_getter_money(self):
        self.assertEqual(100, self.wallet.get_money())

    def test_setter_money(self):
        self.wallet.set_money(10)
        self.assertEqual(10, self.wallet.get_money())

class TestEngine(unittest.TestCase):
    def setUp(self):
        self.eng = Engine(1,1)

    def test_update(self):
        self.eng.update(10)
        self.assertEqual(11, self.eng.status()[0])

    def test_status(self):
        self.assertEqual([1, 1], self.eng.status())

if __name__ == '__main__':
    unittest.main()
