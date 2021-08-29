import smtplib, ssl
# from sca import sendEmails, emailAddress, emailPassword, smtp server

sendEmails = True
emailAddress = "sender@gmail.com"
emailPassword =  "senderPW"
smtp_server = "smtp.gmail.com:465"
emailAddressReceiver = "receiver@gmail.com"

header = "Subject: Schnucks Coupon Applier\n"
errorOccurred = "\nError occured while trying to login. Please make sure credntials are correct and the script is up to date."
beforeCoupons = "\nValue of coupons before: "
afterCoupons = "\nValue of coupons after: "
footnote = "\n\nhttps://github.com/SrgElephant/Schnucks-Coupon-Applier\n"

before = "$69"
after = "$5645634"

def sendEmail(sendSuccessEmail = False):
    if(sendEmails):
        if(sendSuccessEmail):
            body = header + beforeCoupons + before + afterCoupons + after + footnote
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

sendEmail()
sendEmail(True)
