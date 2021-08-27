from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time, sys

# TODO provide credentials
SchnucksAcctEmail = "abc@gmail.com"
SchnucksAcctPassword =  "abc"

# TODO set sendEmails to True if desired; must provide email account credentials
sendEmails = False
emailAddress = "abc@gmail.com"
emailPassword =  "abc"

def getCouponTotal(driver, status):
    driver.refresh()
    time.sleep(5)
    couponSavings = driver.find_element_by_css_selector("div.link-text").text;
    print(status + ": " + couponSavings)
    return couponSavings

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

# Get current value of coupons
valueBeforeClicking = getCouponTotal(driver, "Before")

# Find all the unclipped coupons and click them
unclippedCoupons = driver.find_elements_by_class_name('schnucks-red-bg')
numOfUnclippedCoupons = len(unclippedCoupons)

# '- 1' due to the hidden button
print("Number of coupons clicked: " + str(numOfUnclippedCoupons - 1))

# start at 1 to ignore the hidden button
for i in range(1,numOfUnclippedCoupons):
    unclippedCoupons[i].click()

# Update the impact of the coupons
valueAfterClicking = getCouponTotal(driver, "After")

# Send email of before / after coupon values

# driver.close()
