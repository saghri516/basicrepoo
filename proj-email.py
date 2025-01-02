#This is my email chec

import smtplib as s
ob=s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('saghriktk5@gmail.com','57486470SAG')
subject="python"
body='hello'
massage='subject:{}\n\n{}'.format(subject,body)
listadd=("ktksiraj925@gmail.com")
ob.sendmail('saghriktk8@gmail.com',listadd,massage)
print("done")