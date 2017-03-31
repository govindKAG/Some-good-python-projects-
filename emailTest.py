import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("kagarmy@gmail.com", "iamkaghellyeah")
 
msg = "this is all teh message there is today i am afraid"
server.sendmail("kagarmy@gmail.com", "govindsomalal7@gmail.com", msg)
server.quit()
