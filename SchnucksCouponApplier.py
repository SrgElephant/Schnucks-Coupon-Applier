from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time, sys, smtplib, ssl

# TODO provide credentials
SchnucksAcctEmail = "SchnucksAcct@gmail.com"
SchnucksAcctPassword =  "SchnucksAcct"

# TODO set sendEmails to True if desired; must provide email account details
sendEmails = True
emailAddress = "sender@gmail.com"
emailPassword =  "senderPW"
emailAddressReceiver = "receiver@gmail.com" # can be identical to emailAddress
smtp_server = "smtp.gmail.com:465"

# --- Setup done - No modifications required after this line ---
header = "Subject: Schnucks Coupon Applier\n"
errorOccurred = "\nError occured while trying to login. Please make sure credentials are correct and the script is up to date."
beforeCoupons = "\nValue of coupons before: "
appliedCoupons = "\nNumber of coupons applied: "
afterCoupons = "\nValue of coupons after: "
footnote = "\n\nhttps://github.com/SrgElephant/Schnucks-Coupon-Applier\n"

def getCouponTotal(driver):
    driver.refresh()
    time.sleep(5)
    couponSavings = driver.find_element_by_css_selector("div.link-text").text;
    return couponSavings

def sendEmail(sendSuccessEmail = False):
    if(sendEmails):
        if(sendSuccessEmail):
            body = header + beforeCoupons + valueBeforeClicking + appliedCoupons + numOfUnclippedCoupons + afterCoupons + valueAfterClicking
        else:
            body = header + errorOccurred
        try:
            server = smtplib.SMTP_SSL(smtp_server)
            server.login(emailAddress, emailPassword)
            server.sendmail(emailAddress, emailAddressReceiver, (body + footnote))
        except Exception as e:
            print(e)
        finally:
            print("Sent\n" + body)
            server.quit()
    else:
        print("sendEmails set to False")

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
    sendEmail(False)
    driver.close()
    sys.exit()

# Navigate to the coupons page
driver.get("https://nourish.schnucks.com/web-ext/coupons")

# Get current value of coupons
valueBeforeClicking = getCouponTotal(driver)

# Find number of unclipped coupons
unclippedCoupons = driver.find_elements_by_class_name('schnucks-red-bg')
# '- 1' due to the hidden button
numOfUnclippedCoupons = str(len(unclippedCoupons) - 1)

# click buttons
driver.execute_script("let btns = document.querySelectorAll('.schnucks-red-bg');btns.forEach(btns => btns.click())")
time.sleep(5)

# Update the impact of the coupons
valueAfterClicking = getCouponTotal(driver)

# Send email of before / after coupon values
sendEmail(True)

# driver.close()
