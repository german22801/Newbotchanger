
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

def get_prediction():
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)

        driver.get("https://1wqjnb.com/casino/play/1play_1play_luckyjet?p=7of1")
        time.sleep(3)
        
        # Вход
        email_input = driver.find_element(By.NAME, "email")
        email_input.send_keys("germanbylaev18@gmail.com")
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys("DED1029384756ded")
        driver.find_element(By.CLASS_NAME, "submit").click()
        time.sleep(5)

        # Заглушка коэффициентов
        coefficients = [1.23, 1.45, 1.87, 2.03, 1.56]
        avg = sum(coefficients) / len(coefficients)
        suggestion = "Продавать на x{:.2f}".format(avg * 0.9)

        driver.quit()
        return f"Последние коэффициенты: {coefficients}\nСреднее: {avg:.2f}\n{suggestion}"
    except Exception as e:
        return f"Ошибка при получении данных: {str(e)}"
