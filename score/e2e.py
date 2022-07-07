from selenium import webdriver
from selenium.webdriver.common.by import By


def test_scores_service():
    sc = webdriver.Chrome(executable_path="C:/web drivers/chromedriver.exe")
    sc.get("http://127.0.0.1:5000/")
    mys = sc.find_element(By.XPATH, '/html/body/h1/div').text
    mys = mys.isnumeric()
    if mys:
        if 0 < mys < 1000:
            return True
        return False


def main_function():
    if test_scores_service():
        print("0")
    else:
        print("-1")


main_function()
