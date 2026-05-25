def check_string(s1, s2, s3):
    if s1.startswith("The") or s2.startswith("The") or s3.startswith("The"):
        return "Found it!"
    else:
        return "Nope!"
print(check_string("the man","pot","birds"))
print(check_string("the guy","the lady","the kid"))
print(check_string("The guy","The lady","The kid"))
