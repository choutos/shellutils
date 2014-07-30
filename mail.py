#!/usr/bin/env python

import sys
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email import Encoders
import smtplib,os

MAILHOST = 'localhost'
FROMADDR = "from@example.com"
TOADDR = "someone@example.com"
ZIPFILENAME = str(sys.argv[1])


mssg = MIMEMultipart()
mssg['Subject'] = "This is the subject "
mssg['To'] = TOADDR
part = MIMEBase('application',"octet-stream")
part.set_payload(open(zipFileName,"rb").read())
Encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="%s"' %
os.path.basename(ZIPFILENAME))
mssg.attach(part)

s = smtplib.SMTP(MAILHOST)
#s.set_debuglevel(1)
s.sendmail(FROMADDR,TOADDR,mssg.as_string())
s.quit()

