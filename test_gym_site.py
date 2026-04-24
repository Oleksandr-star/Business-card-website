import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://oleksandr-star.github.io/Business-card-website/"

class GymSiteTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        cls.driver.get(BASE_URL)

    def test_successful_title(self):
        """Успішний тест: перевіряє наявність заголовка GYMASSISTANT"""
        heading = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertIn("GYMASSISTANT", heading.text.upper())
        print("✅ Тест 1 (заголовок) пройдено")

    def test_navbar_exists(self):
        """Успішний тест: перевіряє, що навігаційне меню відображається"""
        nav = self.driver.find_element(By.CLASS_NAME, "navbar")
        self.assertTrue(nav.is_displayed())
        print("✅ Тест 2 (навбар) пройдено")

    def test_find_nonexistent_button(self):
        """Провальний тест: шукає неіснуючий елемент (очікувано падає)"""
        self.driver.find_element(By.ID, "delete-all")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()