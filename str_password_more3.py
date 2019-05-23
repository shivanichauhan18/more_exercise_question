password=raw_input("enter your password ")
if (len(password)<=6) or (len(password)<16):
    if "Z" in password or "A" in password:
        if str(1) in password or str(8) in password:
            print "its strong password"
else:
    print "not strong"