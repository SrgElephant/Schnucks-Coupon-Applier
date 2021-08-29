import smtplib, ssl
from SchnucksCouponApplier import sendEmails, emailAddress, emailPassword, emailAddressReciever, smtp_server, valueBeforeClicking, valueAfterClicking

header = "Subject: Schnucks Coupon Applier\n"
errorOccurred = "\nError occured while trying to login. Please make sure credntials are correct and the script is up to date."
beforeCoupons = "\nValue of coupons before: "
afterCoupons = "\nValue of coupons after: "
footnote = "\n\nhttps://github.com/SrgElephant/Schnucks-Coupon-Applier\n"

def sendEmail(sendSuccessEmail = False):
    if(sendEmails):
        if(sendSuccessEmail):
            body = header + beforeCoupons + valueBeforeClicking + afterCoupons + valueAfterClicking + footnote
        else:
            body = header + errorOccurred + footnote
        try:
            server = smtplib.SMTP_SSL(smtp_server)
            server.login(emailAddress, emailPassword)
            server.sendmail(emailAddress, emailAddressReceiver, body)
        except Exception as e:
            print(e)
        finally:
            print("Sent\n" + body)
            server.quit()
    else:
        print("Not Sending")
