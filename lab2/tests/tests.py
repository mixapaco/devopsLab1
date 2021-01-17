import unittest
from app import main
from app import home_work


class TestClass(unittest.TestCase):
    def setUp(self):
        # Дана функція налаштовує початкові агрументи визначені лише для класу
        self.date_url = 'http://date.jsontest.com/'
        self.ip_url = 'http://ip.jsontest.com/'

    def test_date_work_successfully(self):
        # Перевіряєм чи функція відправювала до кінця і повернулі True
        self.assertTrue(main(self.date_url))

    def test_empty_url(self):
        # Перевіряєм чи у функцію не було передано жодної URL
        self.assertFalse(main())

    def test_no_date_in_response(self):
        # Перевіряємо що у відповіді відсутнє поле дата (тобто передана направильна URL)
        with self.assertRaises(Exception):
            main(self.ip_url)

    def test_home_work(self):
        # Ваш захист
        # Перувірка на пусте значення дати
        self.assertFalse(home_work(False))

        # Перувірка на ніч
        d = {"time" : "03:14:49 PM"}
        self.assertTrue(home_work(d))

        # Перувірка на день
        d = {"time" : "03:14:49 AM"}
        self.assertTrue(home_work(d))

        # Перувірка на неправильний запис
        d = {"time" : "03:14:49 AS"}
        self.assertFalse(home_work(d))

        # Перувірка на неправильний формат
        d = {"time" : "03:14:49"}
        self.assertFalse(home_work(d))


