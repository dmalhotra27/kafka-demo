from unittest import TestCase
from kafka.errors import KafkaError
import producer


class Test_send_json_data (TestCase):
    # simulate NOK case for input data
    def test_send_json_data_NOK(self):
        fname = 'input.json'
        self.assertRaises(IOError, producer.send_json_data(fname))

    # simulate OK case for input data
    def test_send_json_data_OK(self):
        fname = 'input-data.json'
        self.assertNotEqual(IOError, producer.send_json_data(fname))
