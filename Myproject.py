import math
import datetime
import sys
import webbrowser
import platform
import hashlib
import socket
import os
import os.path
## logo = 5 WhiteSpaces



today = datetime.datetime.now()
print("""\n\n 

   __         __             ______        ___            ___            __          _____            ________________ 
  |  |       |  |           / ___ \        \  \          /   \          / /         /  ___ \          |  |____________|
  |   \      |  |          / /   \ \        \  \        /  /\ \        / /         /  /   \ \         |  |
  |   \ \    |  |         / /_____\ \        \  \      /  /  \ \      / /         /  /_____\ \        |  |___________
  |  | \ \   |  |        /  _______  \        \  \    /  /    \ \    / /         /  ________  \       |  |___________|
  |  |  \ \  |  |       /  /       \  \        \  \  /  /      \ \  / /         /  /        \  \      |  |
  |  |   \ \ |  |      /  /         \  \        \  \/ /         \ \/ /         /  /          \  \     |  |  
  |__|    \__|_|      /__/           \__\        \___/           \__/         /__/            \__\    |__| 
                                     
                                      
                                      -- V e r s i o n   1.0  -- 
              \_____/
              ( * * )                       | Welcome To Nawaf Tools |
          _  |-------|  _
         | | |       | | |
         | | |       | | |                  [+] Created By Nawaf [+]
         |_| |_______| |_|                  
               _    _                        || G i T H U B |
              |  | | |                 
              |_|  |_|                 [+] https://github.com/Nawaf404 [+]
                                
""")
now = datetime.datetime.now()
NameDay = now.strftime("%A")
DateT = datetime.datetime.now().day
DateM = datetime.datetime.now().month
DateMonthName = datetime.datetime.now()
Monthname = DateMonthName.strftime("%B")
YearDate = datetime.datetime.now().year
slash = " / "
whitespaces = " "
Date = NameDay + whitespaces + str(DateT) + whitespaces +  Monthname + whitespaces + slash + whitespaces +str(DateM)+ whitespaces + slash +whitespaces+ str(YearDate)
print("Date Today :\n\n {} ".format(Date))

today = datetime.datetime.now().today()
print("\n\n Current date Today : \n\n" , today)


print('''\n\n                                 Welcome          \n\n''')
print("                              Tools | Nawaf |   \n")
print("""                            |---------------------|
                            |                     |
                            |  WE WATCHING YOU    |
                            |                     | 
                            |       \_____/       |
                            |       ( *  * )      |
                            |        \_==_/       |
                            |_____________________|""")
admin = socket.gethostname()
IPadmin = socket.gethostbyname(admin)
print("\n\nYour Computer Name is : " , admin , "\n\nYour iP Address : " , IPadmin)
## قسيم الاوامر الى قسمين , سايبر سكيورتي + حروف + ماث
print("\n========================================")
print("\n\n")
One = True
while True:

    try:
            First_name = str(input("Whats ur First Name : "))
            Last_name = str(input("\nand Last Name :  "))
            print("\nYour Welcome ", First_name + " " + Last_name, " ! ")
            pass
            break
            One = True
    except KeyboardInterrupt as ty:
                    print("Do you Kidding with me ? " , ty)
    except TypeError as Erms:
                print("Try again : ", Erms)
print("\n\n     Wish to you Nice Day ! \n\n")
print("\n||=========================================================================")
Section = input("\n\n||   Choose Any Section What You Want :)               |+|\n\n\n"
      "|-|       A  -  Basic Python  ( Letters and statement )               |+|\n\n"
      "|-|       B  -  Mathmatics                                            |+|\n\n"
      "|-|       C  -  Cyper Security                                        |+|\n\n"
      "|-|       D  -  Info in Programming                                   |+|\n\n"
      "|-|       E  -  Sources for Learn                                     |+|\n\n"
      "|-|       F  -  Live Programming Experience !                         |+|\n\n"
      "|-|       @ -   Info My Combuter                                      |+|\n\n"
      "|-|       H -   Contact Us                                            |+|\n\n"
      "|-|       M - i have Msg for you :)                                   |+|\n\n"
      "|-|       00 - Exit ()                                                |+|\n"
      "|-|___________________________________________________________________|+|\n\n"
                "root@kali ; ")
print("========================================")
if Section == "00":
    exit()
## info programm = ( * ) is Multi and \ is Div
if Section == "A":
    print("""          
                         //--\\        ________
                        / /  \ \       ||     \\
                       / /____\ \      ||      \\
                      / /______\ \     ||______||
                     / /        \ \    ||------\\
                    /_/          \_\   ||       ||
                                       ||_______//
                    """)
    SecA = input("Choose Any Option : \n\n"
                 "          1 - Split Words\n\n"
                 "          2 - Count the word in Text .\n\n"
                 "          3 - Len words\n\n"
                 "          4 - CAPITILAZ WORDS\n\n"
                 "          5 - Title Text\n\n"
                 "          6 - Replace Words\n\n"
                 "          7 - Delete whitespaces\n\n"
                 "          8 - Repeat Text\n\n"
                 "          9 - Count from 1 - 99 \n\n"
                 "          10 - Dictionary Python\n\n==> ")
    if SecA == "1":
        print("\nExample ==> \n{\n\n    Math\n\n    English\n\n Computer Science\n\n    Biolgy\n}")
        print('============')
        split_word = input('\ntype words here to split ==> :\n')
        arr = split_word.split(' ')
        for element in arr:
            print(element)

    if SecA == "2":
        DefultOrSelf = input("\nWelcome ..\nDo you want Defult Text or From You ? \n\n1 - Defult\n2 - From me\n==> ")
        if DefultOrSelf == "1":
            textDefult = "\n\nA lot is happening in the world of Python. Support for Python 2 is\n ending, more and more companies \nare referencing Python in job descriptions and it \ncontinues to gain new libraries and more support.\nSince there is so much changing so fast, we got some of our favorite articles. We hope they help you on your Python programming journey."
            print(textDefult)
            print("\n\nI will Search in word 'Python' ")
            word_in_text = "Python"
            if word_in_text in textDefult:
                print("\nfound it ! >>> ", textDefult.count(word_in_text), word_in_text)


        if DefultOrSelf == "2":
            count = input("enter text to count ==> ")
            whats_word = input("what's word you want count it ? ")
            if whats_word in count:
                print("i found it : ", whats_word)
            if whats_word not in count:
                print("not here . ")
            print(count.count(whats_word))

    if SecA == "3":
            print("\n \nWelcome !\n")
            print('''Note : ''' "len = that mean to count letters\nExample ==> Count letter\n==> ")
            lenWord = input("Type words to len it >>>\n")
            x_len = len(lenWord)
            print("\n",x_len)

    if SecA == "4":
            print("Make All of Letters is Capitial \nExample : HELLO WORLD\n")
            Upper = input("Enter Word ==> ")
            print(str.upper(Upper))
            Capi = input("and Do you want Lower All of Letters ? [ Y / n ] \n>>>")
            if Capi == "Y":
                print(str.lower(Upper))
    if SecA == "5":
            print("Make first Letter Capital \nExample : Hello World\n")
            TitleCap = input("Enter Text >>>")
            print(str.capitalize(TitleCap))
    if SecA == "6":
            print("Always We see Nice Words and We want Replace some Words to Best ! \nLike This : Java is the Best\n-Java\nAfter Replace :\nPython is The Best !\n-Python ")
            Rep = input("Enter Text : ")
            RepW = input("Enter Words To Replace it : ")
            RepTp = input("Enter Words You want in Text instead Old :\nLike : Old ( Java ) New ( Python )\n>>> ")
            print(Rep.replace(RepW , RepTp))
    if SecA == "7":
            EAC = input("Do you want Delete Whitespaces in :\n1 - Start Text\n2 - End Text\n3- All of Whitespaces\n>>> ")
            if EAC == "1":
                EACall = input("Enter Text >>> ")
                print(EACall.lstrip())
            if EAC == "2":
                EACend = input("Enter Text >>> ")
                print(EACend.rstrip())
            if EAC == "3":
                EACstart = input("Enter Text >>> ")
                print(EACstart.strip())
                print("\n\nYour Welcome ! ")

    if SecA == "8":
            print("Welcome ! \n\nYou Can Repeat your name\n\nExample : Python Python Python Python Python\nThere s Were Repeat Python 5 times and You Can Do it ! ")
            NameRep = str(input("\n\nEnter Ur Name : "))
            RepName = int(input("\n\nEnter how many to Repeat ; "))
            Re2 = NameRep * RepName
            print(Re2.strip(' '))
    if SecA == "9":
            ## Count from 1 - 99
            i = 1
            CountNumberUser = int(input(" Type number >>> "))

            cut = input("Choose Word To show in Count : \n1 - Name\n2 - Thanks\n3 - Nice Day\n4 - Or what you want :) \n>>>")
            if cut == "1":
                names = input("Enter Your Name : ")

            while i < int(CountNumberUser):
                print(names , " : ", i)
                i += 1
            if cut == "2":
                while i < int(CountNumberUser):
                    print("Thanks : ", i)
                    i += 1
            if cut == "3":
                while i < int(CountNumberUser):
                    print("Nice Day : ", i)
                    i += 1
            if cut == "4":
                typeCount = input("Type words for show in count >>> \n ")
                while i < int(CountNumberUser):
                    print(typeCount , i)
                    i += 1
            if cut == " ":
                while i < int(CountNumberUser):
                    print("Number : ", i)
                    i += 1

    if SecA == "10":
        print('''\nWelcome to Dict Python ()\n''')


        def main():
            dict()
            while True:
                dic = {'name': 'python', 'age': '1991', 'License': 'openSource', 'in What Using ? ': 'web,GUI,Scripting, Applaction Mobile , Networks , Security System', 'Level Laungage'
                : 'high', 'whats code for display on Screen?': 'print'}
                Words = ("      - name :\n\n       - age:\n\n     - License :\n\n     -in What Using :\n\n        - Level Laungage :\n\n      - whats code for display on Screen :\n\n")
                print(Words, "\n\n\n", "choose", "\n\n")
                userdict = input("Type word : ")
                Transfer = dic.get(userdict)
                print("\n\n====>  ",Transfer , "  <====")
                print("\n\n", " W e l c o m e ! ", "\n")
                return True
        main()
if Section == "B":
    print(""" 
               < / > 
     """)
    Mathmetic = input("Choose Any Options :\n\n"
                      "        1 - Numbers\n"
                      "        2 - How Old i am"
                      "        3-Bigger or Smaller\n\n==> """)
    if Mathmetic == "1":
        MathOp = input("Choose Any Opreate :\n"
                       "1 - Add\n"
                       "2 - Minus\n"
                       "3 - Multiply\n"
                       "4 - Div\n\n==>")
        if MathOp == "1":
            while True:
                try:
                    sum1 = int(input("Enter Num 1 : "))
                    sum2 = int(input("Enter Num 2 : "))
                    TotalAddc = (sum1 , " + " , sum2)
                    print(TotalAddc)
                    TotalAdd = sum1 + sum2
                    if sum1 + sum2 is not str:
                        print("\n( ",TotalAdd," )")
                except ValueError as add:
                    print("Bad Input : ", add)
                    break
                break
        if MathOp == "2":
            while True:
                try:
                    sum3 = int(input("Enter Num 1 : "))
                    sum4 = int(input("Enter Num 2 :"))
                    if sum3 + sum4 is not str:
                        TotalAddcm = ( sum3 , " - " , sum4)
                        print(TotalAddcm)
                        TotalMinus = sum3 - sum4
                        print("\n( ",TotalMinus," )")
                except ValueError as Min:
                    print("Bad Input : " , Min)
                    break
                break
        if MathOp == "3":
            while True:
                try:
                    sum5 = int(input("Enter Num 1 :"))
                    sum6 = int(input("Enter Num 2 :"))
                    if sum5 + sum6 is not str:
                        TotalMult = (sum5 , " * " , sum6)
                        print(TotalMult)
                        TotalMultsc = sum5 * sum6
                        print(TotalMultsc)
                except ValueError as Mult:
                    print("Bad Input : ", Mult)
                    break
                break

        if MathOp == "4":
            while True:
                try:
                    sum7 = int(input("Enter Num 1 :"))
                    sum8 = int(input("Enter Num 2 :"))
                    if sum7 + sum8 is not str:
                        TotalDiv = (sum7 , " / " , sum8)
                        print(TotalDiv)
                        TotalDivs = sum7 / sum8
                        print(TotalDivs)
                except ValueError as div:
                    print("Bad Input : ", div)
                    break
                break
    if Mathmetic == "2":
        ## How My Old
        print('''Welcome ''')
        ChooseOld = input(
            "Do you want know ur old By Birth Years Or Just type Ur Old\n1- Type BirthYears\n2- I just know my Old\n>>>")
        if ChooseOld == "1":
            MyOld = input("When you Birth ? ")
            Birth = datetime.datetime.now().year
            total = Birth - int(MyOld)
            print("Your age is : {}".format(total))
        if ChooseOld == "2":
            MyOld2 = input("How your Old >>> ")
            UserOld = datetime.datetime.now().year
            totalOld = UserOld - int(MyOld2)
            print("Your BirthDay is {}".format(totalOld))

    if Mathmetic == "3":
        print('''\n\nWelcome in bigger or smaller\nroot@math ;  ''')
        b_s = input("\n\nChoose Any Opreater :\n\n1 - bigger of than\n\n2 - smaller of than\n\n3 - equal or not\n\n\nroot@math ; ")
        if b_s == "1":
            print('''\n< /  B I G G E R  > \n\nExample:\nif Num > (Big of than ) Num2 ?\nprint( Yeah , Num1 is bigger )\n\n''')
            bg = int(input("Type Number : \nroot@math ; "))
            bg2 = int(input("Type Number 2 : \nroot@math ; "))
            if bg > bg2:
                print("[ + ] Yeah !\n it's Bigger [ + ]\n\n")
                print(bg , "It's Bigger of " , bg2)
            else:
                print("\n\nNo , it's smaller ")
                print(bg , "it's smaller of " , bg2)

        if b_s == "2":
            print('''\n< / smaller > \nExample :\nif Num1 < (small of than Num2)\nprint( Yeah , Num1 is smaller )\n\n\n''')
            sm = int(input("Type Number 1 : \n\nroot@math ; "))
            sm2 = int(input("Type Number 2 :\n\nroot@math ; "))
            if sm < sm2:
                print("[ + ] Yeah ! its smaller\n\n ")
                print(sm , 'its smaller of ' , sm2)

if Section == "C":
    LogoC = """ \n\n\n
                        \-\               /-/     \n
                         \ \             / /      \n
                          \_\___________/_/       \n
                           /             \        \n
                          /  ( * ) ( * )  \       \n
                         /                 \      \n
                        |                   |     \n
                        \       < / >       /     \n
                         \_________________/      \n
                                                  \n
                         
                         
                         """
    print(LogoC)
    CyperSecurity = input("\n\n\n\nWelcome in CyperSecurity\n\n"
                          "Choose Options :\n\n"
                          "1 - Get iP Address\n\n"
                          "2 - Get Mac Address\n\n"
                          "3 - Crypto Password\n\n"
                          "4 - Search in Google\n\n"
                          "5 - Create File\n\n"
                          "6 - Encryption File\n\n"
                          "7 - Scanner Port\n\n"
                          "0 - Cyper\n\nroot@kali ; ")
    if CyperSecurity == "0":
        print("""                 0                        0
                       1    0                    1    0
                      0      1                  0     1
                     1       0                 1      0
                     0      '  1              0     ' 1
                      0   '     0 1 0 0 1 0 1 ' ' '  0
                       1 '                           1
                       0                            0 
                       1      ______     _____      1
                       0     /( 0 )\    /( O )\     1
                       1                            0
                        1             0            1
                          0101010101010101010101010 
                           11010101010101010101010 
                            001010101010101010100
                             1010101010101010101
                              00101010101010100
                               1010101010101011
                                0010101010100
                                  1555555551
                                     0 0



                   <  /   > 


           ++++ Coung .. You Have Complete The CTF - Challenge ++++
                       """)
    if CyperSecurity == "1":
        print("\n\n=== W E L C O M E ===\n\n")

        print(           "||===================================||\n"
                         "||                                   ||\n"
                         "||           Enter Target =>         ||\n"
                         "||                                   ||\n"
                         "||===================================||\n")
        while True:
            try:
                hostname = input("\n\n[+] Target [+] >>> ")
                ip = socket.gethostbyname(hostname)
                print("\n\nhostname => ", hostname, "\n\n", "iP host => ", ip)
            except socket.gaierror as web:
                print("Not Found website : " , web)
            else:
                break
        req = input("\n\nDo you want Show Website in Chrome ?, [Y or N] : ")
        if req == "Y":
            print("\nOk\n")

            cURL = "https://google.com/search?q="
            openCH = webbrowser.open(cURL + hostname)
            print(openCH)
    if CyperSecurity == "2":
        import re, uuid

        # joins elements of getnode() after each 2 digits.
        # using regex expression
        print("[+] The MAC address is [+] : ", end="")
        print(':'.join(re.findall('..', '%012x' % uuid.getnode())))
    if CyperSecurity == "3":
        print(''' W E L C O M E ''')
        print("Crypto Password ==> \n")
        ChooseCrypto = input("What you want type of Crypto >>\n\n1 - md5()\n"
                             "2 - sha1()\n"
                             "3 - sha224()\n"
                             "4 - sha384()\n"
                             "5 - sha512()\n>>>\n")
        if ChooseCrypto == "1":
            passwordm= input("Please Enter the password : ")
            byte_Password = bytes(passwordm, 'utf-8')
            hash_password = hashlib.md5(byte_Password)
            new_Password = hash_password.hexdigest()
            print(new_Password)

        if ChooseCrypto == "2":
            passwords1 = input("Please Enter the password : ")
            byte_Password = bytes(passwords1, 'utf-8')
            hash_password = hashlib.sha1(byte_Password)
            new_Password = hash_password.hexdigest()
            print(new_Password)

        if ChooseCrypto == "3":
            passwords3 = input("Please Enter the password : ")
            byte_Password = bytes(passwords3, 'utf-8')
            hash_password = hashlib.sha224(byte_Password)
            new_Password = hash_password.hexdigest()
            print(new_Password)

        if ChooseCrypto == "4":
            passwords384 = input("Please Enter the password : ")
            byte_Password = bytes(passwords384, 'utf-8')
            hash_password = hashlib.sha384(byte_Password)
            new_Password = hash_password.hexdigest()
            print(new_Password)
        if ChooseCrypto == "5":
            passwords55 = input("Please Enter the password : ")
            byte_Password = bytes(passwords55, 'utf-8')
            hash_password = hashlib.sha512(byte_Password)
            new_Password = hash_password.hexdigest()
            print(new_Password)

    if CyperSecurity == "4":
        import webbrowser

        print("=== Welcome To Search === ")
        url = input("Enter word for search ==>  ")
        tapURL = "https://google.com/search?q="
        qe = webbrowser.open(tapURL + url)
        print(qe)

    if CyperSecurity == "5":
        print("""       |===================================|\n
                    |                                   |\n
                    |   Names Files With ( . txt )      |\n
                    |           - File.txt              |\n
                    |+++++++++++++++++++++++++++++++++++|\n""")
        save_file = "C:/Desktop/"
        CreateFile = input("\nWhat you would to name your file : \n\nroot@files ; ")
        EditFile = (CreateFile + '.txt')
        CompleteName = os.path.join(save_file, EditFile)
        UserFile = open(CreateFile, 'w+')
        print("\nDone !\n")
        WriteOnFile = input("\nWhat you would to write into file : \nroot@files ;  ")
        UserFile.write(WriteOnFile)
        print("\nDone !\n")
        UserFile.read()
        while True:
            try:
                ReadTheFile = input("\nDo you want read the File ?  [ Y / n ] :\nroot@files ; ")
                if ReadTheFile == "N":
                    exit()
                if ReadTheFile == "Y":
                    print("\nRemember : Your name file is (", CreateFile, ")\n")
                    fileToOpen = input("\nEnter name file : ")
                    with open(fileToOpen, mode='r') as f:
                        for line in f:
                            line = line.strip()
                            print("Text //\n\n\n",line,"\n\n\nEnd ..")
                            break
                        break
            except FileNotFoundError as ndd:
                print("File don't found : " , ndd)
    if CyperSecurity == "6":
        import hashlib
        from hashlib import md5
        from hashlib import sha256
        from hashlib import sha512
        from hashlib import sha384
        print("""
                  _________
                  ||-----||
                  ||     ||
               ---------------
               |    _____    |
               |   | * * |   |
               |    \___/    |
               |             |
               ---------------
               
               
        """)
        while True:
            try:

                EnterUser = input("Enter File : \nroot@files ; ")
                with open(EnterUser , mode='r') as read:
                    for linep in read:
                        linep = linep.strip()
                        print(linep)
                        break
                    break
            except ValueError as send:
                print("Not found file : " , send)
            except KeyboardInterrupt as key:
                print("BAD KEYBOARD !  : You Trying to Escape :) " , key)
            except NotADirectoryError as ee:
                print("There's Problem : " , ee)
            except FileNotFoundError as file:
                print("File Not Found : " , file , "\nSolution :\nBack To Option 5 (Create Files) and Create file \n")
                exit()
        print("""                /\
                                 ||
                                 ||
                    
                |=============================|   
                |    Text before Cryption     |
                |=============================|
                
                ...............................
                
                |==============================|
                |    Text after Crpytion       |
                |==============================|
                
                            ||
                            ||
                            \/
        
                 """)
        from hashlib import md5
        with open(EnterUser, 'w') as Ef:
            for line in EnterUser:
                line = line.strip()
                hashp = md5(line.encode()).hexdigest()
                print(hashp)
                #"2 - sha1()\n"
                             #"3 - sha224()\n"
                             #"4 - sha384()\n"
                             #"5 - sha512()\n>>>\n")
        cp = input("[+]  Choose Type Crypation  [+]\n\n"
                   "    || Note : In First Time will Crypation with md5() auto ||\n\n"
                   "    1 - sha256()\n\n"
                   "    2 - sha384()\n\n"
                   "    3 - sha512()\n\nroot@kali ; ")
        if cp == "1":
            EnterUser_sha256 = input("Enter File : \nroot@files ; ")
            with open(EnterUser_sha256, mode='r') as read:
                for line256 in read:
                    line256 = line256.strip()
                    print(line256)
            print(LogoCryp)
            with open(EnterUser_sha256, 'w') as Ef:
                for line25 in EnterUser_sha256:
                    line25 = line25.strip()
                    hashs = sha256(line25.encode()).hexdigest()
                    print(hashs)

        if cp == "2":
            EnterUser_sh384 = input("Enter File : \nroot@files ; ")
            with open(EnterUser_sh384, mode='r') as read:
                for line384 in read:
                    line384 = line384.strip()
                    print(line384)
            print("""                       /\
                                            ||
                                            ||

                           |=============================|   
                           |    Text before Cryption     |
                           |=============================|

                           ...............................

                           |==============================|
                           |    Text after Crpytion       |
                           |==============================|

                                       ||
                                       ||
                                       \/

                            """)
            with open(EnterUser_sh384, 'w') as Ef:
                for line3842 in EnterUser_sh384:
                    line3842 = line3842.strip()
                    hash2 = sha384(line3842.encode()).hexdigest()
                    print(hash2)
        if cp == "3":
            EnterUser_sha512 = input("Enter File : \nroot@files ; ")
            with open(EnterUser_sha512, mode='r') as read:
                for line512 in read:
                    line512 = line512.strip()
                    print(line512)
            print("""                       /\
                                            ||
                                            ||

                           |=============================|   
                           |    Text before Cryption     |
                           |=============================|

                           ...............................

                           |==============================|
                           |    Text after Crpytion       |
                           |==============================|

                                       ||
                                       ||
                                       \/

                            """)
            with open(EnterUser_sha512, 'w') as Ef:
                for line51 in EnterUser_sha512:
                    line51 = line51.strip()
                    hash51 = sha512(line51.encode()).hexdigest()
                    print(hash51)

    if CyperSecurity == "7":
        import socket
        import time
        import threading
        import datetime
        startTime = datetime.datetime.now()
        from queue import Queue
        socket.setdefaulttimeout(0.25)
        print_lock = threading.Lock()

        target = input('Enter the host to be scanned : ')
        t_IP = socket.gethostbyname(target)
        print('Starting scan on host: ', t_IP)


        def portscan(port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                con = s.connect((t_IP, port))
                with print_lock:
                    print(port, 'is open')
                con.close()
            except:
                pass


        def threader():
            while True:
                worker = q.get()
                portscan(worker)
                q.task_done()


        q = Queue()
        for x in range(100):
            t = threading.Thread(target=threader)
            t.daemon = True
            t.start()

        for worker in range(1, 500):
            q.put(worker)

        q.join()
        print('Time taken:', datetime.datetime.now() - startTime)



if Section == "@":
    print("""
                    ______________
                    |    ____     |
                    |_____________|
                    ||           ||
                    ||    Linux  ||
                    ||    \__/   ||
                    ||    (**)   ||
                    ||           ||
                    ||   Windows ||
                    ||   /-\/-\  ||
                    ||           ||
                    ||   MacBook ||
                    ||      _/   ||
                    ||     (_<   ||
                    |_____________|
                    |     ___     |
                    |_____________|
                    
                    
                    """)

    MyNamesComputer = socket.gethostname() # 1
    iPmyComputer = socket.gethostbyname(MyNamesComputer) #6
    MySystem = platform.system() #2
    Uname = platform.uname() #4
    Machine = platform.machine() #8
    BuildPython = platform.python_build()
    Comp = platform.python_compiler()
    VerP = platform.python_version()
    MyProcessor = platform.processor() #7
    Platfor = platform.platform() # 5
    # here's will printed
    print("Your Computer Name : " , MyNamesComputer)
    print("\n\nYour OS : " , MySystem)
    print("\n\nYour system : ", Uname)
    print("\n\nYour Computer : " , Platfor)
    print("\n\nYour IP Address : " , iPmyComputer)
    print("\n\nYour Porcessor is : " , MyProcessor)
    print("\n\nYour Machine is : " , Machine)
    print("\n\nBuild python in : " , BuildPython)
    print("\n\nVersion Python : "  ,VerP)
    print("\n\nCompleier Python : " , Comp)


# info in Programming //
if Section == "D":
    print('''W E L C O M E 
    Here ' s   WE WILL LEARN SOME CODES IN PROGRAMMING :/ 
    
    ''')
    IT = input("1 - Down Line\n\n\n2 - Print On Screen\n\n\n3- tap in Text\n\n\n- and more in Future , i will add a lots in new version\nroot@cmd ; ")
    if IT == "1":
        print("\n\n\nUse Code  \ n  in Python\n\n" 
         "Example : print(Hello\ n World)\n\n" 
         "Output : Hello\nWorld\n\n)\n\n\n")
    if IT == "2":
        print("Use Code ( print ) in python\n" 
        "print( Hello World )")

    if IT == "3":
        print("Use Code  \ t in python\n"
              "Example : print( \ t Hello World )\n"
              "Output :\n   Hello World\nnot will be in start")



if Section == "H":
    print("""   ______________________________________
            -                                         - 
        -                                              -
        -             H E L L O                       -
        '                                           '
         '                                        '
           ' ' ' '  ' '' ' ' ' ' ' ' ' ' ' ' ' ' ' """)
    print("""
    
    
    Contact US  // 
    
    [ + ] GitHub [ + ] 
    
    
    https://github.com/Nawaf404
    
    
    [ + ] Twitter [ + ]
    
     
    @ S K O i i i Z 
    
    Thanks :) """)



if Section == "F":
    print("""Hello in Testing Programming // 
    
    Here's You Can Learn a lots of Codes \\ 
    
    
    Let's Play ! """)

    printOn = input("How do you can print it screen ?\n\nDid you ask yourself before?\n\nOk ! To Print in Screen You have to Type ( Print )\n\nLet's do it\nWrite word Now // ")
    print(printOn, 'its your input\nNow Say print( your word )')
    printPlay = input(" ; ")
    pw = printOn
    print("print ( {} )".format(pw) ,"\nYeah You Can Do it ! ")
    print("\n\nNow for add between 2 Number :\n"
          "Type Num 1  then Num 2 and print it with mark + bewteen them\n\nand remember you must be input int")
    numPlay = int(input("Enter First Num : "))
    num2Play = int(input("Enter Sec Num : "))
    enPlay = input("Now Say print Num1 and Num2 with [ + ]  ")
    print(numPlay + num2Play , "\nYou've Print {} + {} , Great ! ".format(numPlay , num2Play))

    print("\n\nNow Test to Down Line -:\nType word and \ n\n\nExample : Hello\nWorld\n\n")
    LineDown = input("Enter word with \n between words : ")
    print("\n\n" , LineDown , "\n\n")


if Section == "E":
    print("1 - Python BootCamp\n\nhttps://techcampus.com/bootcamp?python\n\n2 - YouTube\n\nhttps://youtube.com/user/TheNewBaghdad\n\n3 - YouTube : Elsafy Hegazy\n\n4 - linkedn \nYasser alosefer in Linkedn\n\n\nand Search in Udemy\n")




if Section == "M":
    print("""Hello World
    /______\
    | *  * |
    \_____/
    
    Bro , I have Msg for you 
    Save it in your heart .. 
    in the Life , is never excited word
    
    
    In this life there is no word impossible, do not be fooled by the losers under the name of this supernatural
If there was something supernatural would not have succeeded one
Success is thinking and patience and try once and twice and three times and indefinitely and up to success
You are successful as long as you are successful
You are now reading this letter This shows that you are a successful person and looking for success
Success is not a cheap commodity
Success is bought only by the patient and those who deposited his time in the attempts
Second, you must have confidence in yourself You must feel that you can and you are strong, you can not succeed as long as hiding under the trees afraid of lightning failure, successful is the one who takes shelter and go despite the difficulties,
All the successful people have been hurt in their beginnings, you have no right to despair and no one else has succeeded in the same success you want

thanks for reading :)
we love you  bro < we need you




.........
if you see any bugs please tell me i will be thank for you <3
""")