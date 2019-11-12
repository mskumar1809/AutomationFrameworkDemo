import pytest
from selenium import webdriver

class TestBaseOrder():

    @pytest.fixture(scope="class")
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="/Users/sampath/PycharmProjects/AutomationFrameworkDemo/drivers/chromedriver")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test Completed")

    def test_navigation(self, test_setup):
        driver.get("https://sgqestaging.circles.asia/plan/pre_checkout")