########################################################################
# R.A.Borrelli
# @TheDoctorRAB
# rev.19.November.2015
# v1.0
########################################################################
#
# Read in a csv file with each email address on a line
# Send an email to each email address
#
########################################################################
#
# imports
#
import smtplib
import numpy
from sys import argv
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.mime.application import MIMEApplication
script,email_list=argv #add a CSV file with email addresses (one on each line) as command line argument
#
########################################################################
#
# email sender
#
sender='r.angelo.borrelli@gmail.com'
#
#######
#
# read in the email addresses
#
email_list=numpy.loadtxt(email_list,dtype=str)
#
#######
#
# loop through the csv to count the email addresses
#
i=0
for line in email_list:
    i=i+1
    email_list_size=i
# end line
#
#######
#
#
#######
#
# SMTP client session start 
#
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,'hrgntcsdnwchgvsk')
#
#######
#
# send the email
#
for j in range(0,email_list_size): #been getting a 'connection unexpectedly closed' error around j=100 
    receiver=email_list[j]
    message=MIMEMultipart()
    message['From']='Bob Borrelli'
    message['To']=receiver
    message['Subject']='ANS UI summer meeting follow up'
    body='''
Hi Everyone,

Thanks for everyone who replied. As I expected, the 27th wasn't a good idea for the next meeting. However, on June 3rd, I have to attend a research workshop all day. How about June 10th then? We actually have things to talk about in terms of setting us up officially with UI (thank you Kelley), and getting together with BYU-UI students (thanks Jared and Malachi, who I will email shortly). 

I'd like to solicit interest in officers as well. Please email me privately to discuss your interest, and we can figure out the next steps after that. I'll keep your names secret until we agree on a voting procedure. 

Finally, we are having a talk at CAES tomorrow afternoon. Please see the attachment. The s

Regards,
Bob
'''    
    part=MIMEApplication(open('caes.talk.pdf','rb').read())
    part.add_header('Content-Disposition','attachment',filename='caes.talk.pdf')
    message.attach(part)
    message.attach(MIMEText(body,'plain'))
    message_text=message.as_string()
#
    server.sendmail(sender,receiver,message_text)
    print j,receiver
# end j
server.quit()
#
########################################################################
#
# EOF
#
########################################################################
