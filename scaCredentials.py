# Version 1.9
# https://github.com/SrgElephant/Schnucks-Coupon-Applier
import rsa

# File
f = open("scaCred.txt", "w")

# Generate keys
publicKey, privateKey = rsa.newkeys(512)
f.write(str(privateKey))
f.write("\n")

# Required input
SchnucksAcctEmail    = input("Schnucks Account email: ")
SchnucksAcctPassword = input("Schnucks Account password: ")
# Encrypt
encSchnucksEmail    = rsa.encrypt(SchnucksAcctEmail.encode(), publicKey)
encSchnucksPassword = rsa.encrypt(SchnucksAcctPassword.encode(), publicKey)
# Write
f.write(str(encSchnucksEmail) + "\n")
f.write(str(encSchnucksPassword) + "\n")

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
	encEmailAddress         = rsa.encrypt(emailAddress.encode(), publicKey)
	encEmailPassword        = rsa.encrypt(emailPassword.encode(), publicKey)
	encEmailAddressReceiver = rsa.encrypt(emailAddressReceiver.encode(), publicKey)
	
	# Write
	f.write(str(encEmailAddress) + "\n")
	f.write(str(encEmailPassword) + "\n")
	f.write(str(encEmailAddressReceiver) + "\n")
	f.write(str(smtp_server) + "\n")
	f.write(str(port) + "\n")

print("Credentials complete.")
f.close()
