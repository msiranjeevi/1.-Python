class ps2():
    def trans(amt):
        if amt > 0:
            print("valid transaction")
        elif amt == 0:
            print("Your balance is zero, please deposit some amount")
        elif amt < 0:
            print("You are fined due to negative balance")
        else:
            pass

    def passcode(pcode):
        # passcode summation must be 49!
        # pcode = int(input("Enter your loacker passcode:"))
        pcode_list = list(str(pcode))
        print(pcode_list)

        pcode_list1 = [int(x) for x in pcode_list]
        print(pcode_list1)
        c = 0
        for i in pcode_list1:
            b = i
            c = c + b
        if c == 49:
            print("Valid passcode, you can access your locker")
        else:
            print("Invalid passcode, entry restricted!!!")
#        print("Total Count:" , c)

    def otp(otp_num):
        print(otp_num)
        otp_list = list(str(otp_num))
        print(otp_list)
        otp_list_r = otp_list[::-1]
        print(otp_list_r)
        print("".join(otp_list_r))
    # prime number check

    def pnc(no):
        if no > 1:
            for i in range(2, no):
                if no % i == 0:
                    print("Its not a prime")
                    break
            else:
                print("Its a prime")
    # else:
    #    print("Its not a prime")

    def fac(fno):
        c = 1
        for i in range(1, fno+1):
            c = c * i
        print(c)

    def arm(no):
        arm_list = list(str(no))
        int_arm_list = [int(x) for x in arm_list]
        print(arm_list)
        print(int_arm_list)
        c = 0
        for i in int_arm_list:
            c = c + (i ** 3)
        if c == no:
            print(c)
            print("Its an armstrong number")
        else:
            print("Its not an armstrong number")

    def pwd(pwd):
        #    pwd='media'
        s_pwd = pwd[-1] + pwd[1:4] + pwd[0]
        return s_pwd

    def bina(bno):
        bno = bin(bno)[2:]
        return bno

    def lwo(sen):

        wds = sen.split()
        print(wds)

        fwo = wds[0]
        for i in wds[1:]:
            if len(fwo) > len(i):
                pass
            elif len(i) > len(fwo):
                fwo = i
        print("The longest word is:", fwo)

    def ana(w1, w2):
        if sorted(w1) == sorted(w2):
            return "Its an anagram"
        else:
            return "Its not an anagram"
