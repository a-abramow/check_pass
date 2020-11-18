def check_password(password):
    count_digit = 0
    count_upper = 0
    count_spec = 0
    for i in password:
        if i.isdigit():
            count_digit += 1

        if i.isupper():
            count_upper += 1

        if i in "!@#$%*":
            count_spec += 1
    print(count_digit, count_upper, count_spec)
    if count_digit >= 3 and count_upper > 0 and count_spec > 0 \
            and len(password) >= 10:
        print("perfect password")
    else:
        print("easy peasy")


check_password('Dfgr123123!')
check_password('dsfwWewfd')
check_password('!"£$%rDFRssdf2ssdsc')
