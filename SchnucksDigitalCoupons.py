from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.close()
