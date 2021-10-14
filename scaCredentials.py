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

# Decide on emails
sendEmails = input("Setup email credentials to send emails (y)?: ")
if sendEmails == "y" or sendEmails == "yes":
	# Optional input
	credentialsStr += input("Sender email address: ") + "\n"
	credentialsStr += input("Sender email password: ") + "\n"
	credentialsStr += input("Receiver email address: ") + "\n"
	credentialsStr += input("SMTP server address\nReccomended: smtp.gmail.com: ") + "\n"
	credentialsStr += input("SMTP server port\nReccomended: 465: ") + "\n"

# Credentials file
f1 = open("cred.txt", "wb")
f1.write(fernet.encrypt(credentialsStr.encode()))
f1.close()
print("Credentials complete.")
