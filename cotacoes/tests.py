import unittest
from datetime import date, timedelta
import requests
import json

class Testing(unittest.TestCase):
    def test_rangeData(self):
        today = date.today()
        for i in range(0,7):
            currentDate =  today - timedelta(days=i)
            if currentDate.weekday() < 5:
                self.assertIsInstance(currentDate, date)
                
    def test_apiRatesDate(self):
        today = date.today()
        response = requests.get('https://api.vatcomply.com/rates?date='+str(today))
        self.assertEqual(response.status_code,200)

    def test_apiValidateJSON(self):
        today = date.today()
        response = requests.get('https://api.vatcomply.com/rates?date='+str(today))
        self.assertEqual(response.status_code,200)
        jsonIsValid = False
        try:
            json.loads((str(response.json())).replace('\'', '\"'))
            jsonIsValid = True
        except ValueError as err:
            print(err)
            jsonIsValid = False
        self.assertTrue(jsonIsValid)

    def test_apiValidateManyRequest(self):
        today = date.today()
        for i in range(0,7):
            currentDate =  today - timedelta(days=i)
            if currentDate.weekday() < 5:
                response = requests.get('https://api.vatcomply.com/rates?base=USD&date='+str(currentDate))
                self.assertEqual(response.status_code,200)

if __name__ == '__main__':
    unittest.main()