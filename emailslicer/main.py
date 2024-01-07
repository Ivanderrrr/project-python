def email_slicer():
    print("EMAIL SLICER \n")
    email = input("enter your email: ")
    
    username, domain = email.split("@")
    domain, extension = domain.split(".")
    
    print("username:", username)
    print("domain:", domain)
    print("extension:", extension)

email_slicer()