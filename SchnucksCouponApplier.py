from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import time, sys

# TODO provide credentials
SchnucksAcctEmail = "abc@gmail.com"
SchnucksAcctPassword =  "abc"

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# Navigate to the page and insert Schnucks credentials
driver.get("https://nourish.schnucks.com/web-ext/user/login?redirectUrl=https:%2F%2Fnourish.schnucks.com%2F")
driver.find_element_by_id('logonId').send_keys(SchnucksAcctEmail)
driver.find_element_by_id('password').send_keys(SchnucksAcctPassword)
driver.find_element_by_class_name('login-button').click()

# Wait for the page to load
time.sleep(5);

# Types of errors
errorLogin = driver.find_elements_by_class_name("login-error")
errorEmail = driver.find_elements_by_class_name("schnucks-red")
if (len(errorLogin) + len(errorEmail) > 0):
    # TODO send email function here
    print("Login failed")
    driver.close()
    sys.exit()
else:
    print("Login successful")

# Navigate to the coupons page
driver.get("https://nourish.schnucks.com/web-ext/coupons")

# Wait for the page to load
time.sleep(5);
couponSavings = driver.find_element_by_css_selector("div.link-text");
previousSavings = couponSavings.text;
print("Before " + previousSavings)


# Find all the unclipped coupons and click them
unclippedCoupons = driver.find_elements_by_class_name('schnucks-red-bg')
numOfUnclippedCoupons = len(unclippedCoupons)
print("Number of coupons to be clicked: " + str(numOfUnclippedCoupons))
for i in range(0,numOfUnclippedCoupons):
    if unclippedCoupons[i].is_displayed():
        unclippedCoupons[i].click();

# Tested

# Update the impact of the coupons
driver.navigate().refresh();
currentSavings = couponSavings.getText();
print("After: " + currentSavings)

# Send email of before / after coupon values
driver.close()
