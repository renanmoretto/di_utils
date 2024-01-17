import random
from unittest import TestCase

import di_utils


class TestTickerVerifier(TestCase):
    def test_random_tickers(self):
        letters = list(di_utils._CONTRACT_LETTERS_MONTH.keys())
        tickers = [f'DI1{letter}{random.randint(10,99)}' for letter in letters]
        for ticker in tickers:
            di_utils.verify_ticker(ticker)

    def test_wrong_contract_letter(self):
        with self.assertRaises(ValueError) as _:
            di_utils.verify_ticker('DI1B30')

    def test_wrong_maturity(self):
        with self.assertRaises(ValueError) as _:
            di_utils.verify_ticker('DI1F3B')

    def test_ticker_wrong_start(self):
        with self.assertRaises(ValueError) as _:
            di_utils.verify_ticker('ABGF3B')
