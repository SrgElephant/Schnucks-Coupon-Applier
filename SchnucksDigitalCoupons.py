from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait

# TODO provide credentials
SchnucksAcctEmail = ""
SchnucksAcctPassword =  ""

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# Navigate to the page and Schnucks credentials
driver.get("https://nourish.schnucks.com/web-ext/user/login?redirectUrl=https:%2F%2Fnourish.schnucks.com%2F")
driver.find_element_by_id('logonId').send_keys(SchnucksAcctEmail)
driver.find_element_by_id('password').send_keys(SchnucksAcctPassword)
driver.find_element_by_class_name('login-button').click()

# Wait until the webpage redirects on successful login
WebDriverWait(driver=driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)

error_message = "Sorry, that login is invalid. Make sure everything is correct and try again. If the problem continues, contact Customer Care."
errors = driver.find_elements_by_class_name("login-error")
if any(error_message in e.text for e in errors):
    print("Login failed")
else:
    print("Login successful")

# Navigate to the coupons page
driver.get("https://nourish.schnucks.com/web-ext/coupons")

# Get the current sum of coupons
WebElement couponSavings = driver.findElement(By.cssSelector("link-text bold-font"));
previousSavings = couponSavings.getText();

# Find all the unclipped coupons and click them
unclippedCoupons = driver.find_elements_by_class_name('.schnucks-red-bg')
for i in range(0,len(unclippedCoupons)):
    unclippedCoupons[i].click();

# Update the impact of the coupons
driver.navigate().refresh();
currentSavings = couponSavings.getText();

# Send email of before / after coupon values
driver.close()
