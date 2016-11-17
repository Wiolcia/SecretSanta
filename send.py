# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from random import shuffle
import numpy as np


# participants.txt and emails.txt have to have the same order (obv)
file_names = open('participants.txt', 'rb')
names = file_names.read()
file_names.close()

file_email = open('emails.txt', 'rb')
emails = file_email.read()
file_email.close()

fp = open('message', 'rwb')
msg_text = fp.read()
fp.close()

email_list = emails.split('\n')
email_list.pop()

names_list = names.split('\n')
names_list.pop()

#draw
a = np.array(names_list)
shuffle(names_list)
test = a==np.array(names_list)
while any(test):
    print 'Test failed. Repeat.'
    shuffle(names_list)
    test = a==np.array(names_list)


save_result= str()
for index, to in enumerate(email_list):
    msg = MIMEText(msg_text % names_list[index])
    
    msg['Subject'] = 'DTC Secret Santa!'
    msg['From'] = 'The Secret Santa Service <wkijewska@gmail.com>'
    msg['To'] =to
    
    s = smtplib.SMTP('localhost')
    s.sendmail(msg['From'], [msg['To']], msg.as_string())
    s.quit()
    save_result+=names_list[index]+' - '+email_list[index]+'\n'


#save the result, just in case

for i in xrange(len(email_list)):
    save_result+=names_list[i]+' - '+email_list[i]+'\n'
file_result = open('do_not_open', 'wb')
file_result.write(save_result)
file_result.close()

