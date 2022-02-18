import smtplib 

smtpServer = "smtp.pepipost.com";

smtpPort = 25;

smtpUsername = "Your_User_Name";

smtpPassword = "Your_Secret_Password";

toAddress = "testuser@mydomain.com";

fromAddress = "from@pepipost.com";

body = """From: From Pepipost <from@pepipost.com>

To: MrRobot <test_recipient@gmail.com>

MIME-Version: 1.0

Content-type: text/html

Subject: SMTP test email

This is an e-mail message to be sent in HTML format using smtplib.

This is HTML message.
This is headline.

"""
mailServer = smtplib.SMTP(smtpServer , smtpPort) mailServer.starttls() mailServer.login(smtpUsername , smtpPassword) mailServer.sendmail(fromAddress, toAddress , body) print(" \n Sent!") mailServer.quit()
