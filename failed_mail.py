import smtplib 
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
# start TLS for security 
s.starttls()   
# Authentication 
s.login("g.gupta1728@gmail.com", "raqu7964HKL") 
# message to be sent 
message = "Hey Developer, you need to check your code once. Might be this have some error. "
# sending the mail 
s.sendmail("g.gupta1728@gmail.com", "san.gupta0312@gmail.com", message) 
# terminating the session 
s.quit()
