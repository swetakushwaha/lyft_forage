import unittest

from engine.sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_with_warning_light_on(self):
        is_warning_light_on = True
        engine = SternmanEngine(is_warning_light_on)
        self.assertTrue(engine.needs_service())

    def test_needs_service_with_warning_light_off(self):
        is_warning_light_on = False
        engine = SternmanEngine(is_warning_light_on)
        self.assertFalse(engine.needs_service())
