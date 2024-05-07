import allure
import pytest


def tear_down():
    print("Class ")


@pytest.mark.sample_test
@allure.title("Sample tests")
class TestSampleTest:

    @pytest.fixture(scope="class")
    def setup(self):
        print("Setup")

    def teardown(self):
        print("teardown")

    def test_test_one(self):
        print("Testing one test ")
        assert True

    def test_test_two(self):
        assert True
