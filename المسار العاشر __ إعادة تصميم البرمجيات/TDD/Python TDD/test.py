import unittest
from unittest import TestCase

from apartment_price_calculator import calculate_apartment_price, regular_price, low_season_rate, high_season_rate, high_season_start_date
from datetime import date, timedelta


class ApartmentPriceTest(TestCase):
    # def test_it_returns_hello_world(self):
    #     self.assertEqual('Hello World!', hello_world())

    def test_number_of_rooms_is_not_negative(self):
        self.assertRaises(ValueError, calculate_apartment_price, -1)

    def test_number_of_rooms_is_not_zero(self):
        self.assertRaises(ValueError, calculate_apartment_price, 0)

    def test_low_season_price(self):
        # Arrange
        a_date = high_season_start_date - timedelta(days=10)
        number_of_rooms = 1

        # Act
        one_room_price = regular_price * low_season_rate
        price = calculate_apartment_price(number_of_rooms, a_date)

        # Assert
        self.assertEqual(one_room_price, price)

    def test_high_season_price(self):

        a_date = high_season_start_date
        number_of_rooms = 1

        one_room_price = regular_price * high_season_rate
        price = calculate_apartment_price(number_of_rooms, a_date)

        self.assertEqual(one_room_price, price)
    def test_date_is_in_future(self):

        a_date = date.today()

        self.assertRaises(Exception, calculate_apartment_price, 1, a_date)

if __name__ == '__main__':
    unittest.main()