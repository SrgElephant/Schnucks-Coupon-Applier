import smtplib, ssl
# from sca import sendEmails, emailAddress, emailPassword, smtp server

sendEmails = True
emailAddress = "abc"
emailPassword =  "abc"
smtp_server = "smtp.gmail.com:465"

header = "Subject: Schnucks Coupon Applier\n"
errorOccurred = "\nError occured while trying to login."
beforeCoupons = "\nValue of coupons before: "
afterCoupons = "\nValue of coupons after: "
footnote = "\nhttps://github.com/SrgElephant/Schnucks-Coupon-Applier\n"

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
            server.sendmail(emailAddress, emailAddress, body)
        except Exception as e:
            print(e)
        finally:
            print("Sent\n" + body)
            server.quit()
    else:
        print("Not Sending")
        
sendEmail()
sendEmail(True)
