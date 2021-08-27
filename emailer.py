import smtplib, ssl
# from sca import sendEmails, emailAddress, emailPassword, smtp server

sendEmails = True
emailAddress = "abc"
emailPassword =  "abc"
smtp_server = "smtp.gmail.com"

header = "Schnucks Coupon Applier\n"
errorMail = "Error occured while trying to login."
beforeMail = "Value of coupons before: "
afterMail = "Value of coupons after: "

before = "$69"
after = "$5645634"

port = 587 # starttls
context = ssl.create_default_context()

def sendErrorEmail(sendEmailBool):
    if(sendEmails):
        print("Sending Error")
        try:
            server = smtplib.SMTP(smtp_server,port)
            server.ehlo()
            server.starttls(context=context)
            server.login(emailAddress, emailPassword)
            server.sendmail(emailAddress, emailAddress, header + errorMail)
        except Exception as e:
            print(e)
        finally:
            server.quit()
    else:
        print("Not Sending")
        
def sendResultEmail(sendEmailBool, before, after):
    if(sendEmails):
        print("Sending Result")
        try:
            server = smtplib.SMTP(smtp_server,port)
            server.ehlo()
            server.starttls(context=context)
            server.login(emailAddress, emailPassword)
            server.sendmail(emailAddress, emailAddress, header + beforeMail + before + "\n" + afterMail + after)
        except Exception as e:
            print(e)
        finally:
            server.quit()
    else:
        print("Not Sending")

sendErrorEmail(sendEmails)
sendResultEmail(sendEmails, before, after)
