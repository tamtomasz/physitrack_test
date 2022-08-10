import pytest

from tests.base_test import BaseTest


class TestDemo(BaseTest):

    def test_demo_account_flow(self):
        driver = self.driver
        print(driver)
