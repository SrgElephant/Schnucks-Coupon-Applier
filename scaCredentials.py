# Version 1.91
# https://github.com/SrgElephant/Schnucks-Coupon-Applier
from cryptography.fernet import Fernet

# Single byte string to be encoded
credentialsStr = ""

# Generate key
key = Fernet.generate_key()
fernet = Fernet(key)

# Key file
f0 = open("key.txt", "wb")
f0.write(key)
f0.close()

# Required input
credentialsStr += input("Schnucks Account email: ") + "\n"
credentialsStr += input("Schnucks Account password: ") + "\n"

# Credentials file
f1 = open("cred.txt", "wb")
f1.write(fernet.encrypt(credentialsStr.encode()))
f1.close()

# Decide on emails
sendEmails = input("Setup email credentials to send emails (y)?: ")
if sendEmails == "y" or sendEmails == "yes":
	# Optional input
	emailAddress         = input("Sender email address: ")
	emailPassword        = input("Sender email password: ")
	emailAddressReceiver = input("Receiver email address: ")
	smtp_server          = input("SMTP server address\nReccomended: smtp.gmail.com: ")
	port                 = input("SMTP server port\nReccomended: 465: ")
	
	# Encrypt
	encEmailAddress         = fernet.encrypt(emailAddress.encode())
	encEmailPassword        = fernet.encrypt(emailPassword.encode())
	encEmailAddressReceiver = fernet.encrypt(emailAddressReceiver.encode())
	
	# Write
	f.write(str(encEmailAddress) + "\n")
	f.write(str(encEmailPassword) + "\n")
	f.write(str(encEmailAddressReceiver) + "\n")
	f.write(str(smtp_server) + "\n")
	f.write(str(port) + "\n")

print("Credentials complete.")
f0.close()
f1.close()
