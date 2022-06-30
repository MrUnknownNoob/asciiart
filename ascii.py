import pyfiglet as pf

print('''

 _____   ____   ____  _____  _____    _____  ____   _____ 
|  _  | / ___| /  __||_   _||_   _|  |  _  ||  _ \ |_   _|
| | | || |__  |  /     | |    | |    | | | || |_| |  | |  
| |_| | \__ \ | |      | |    | |    | |_| ||    /   | |  
|  _  |    | || |      | |    | |    |  _  || |\ \   | |  
| | | | ___| ||  \__  _| |_  _| |_   | | | || | | |  | |  
|_| |_||____/  \____||_____||_____|  |_| |_||_| |_|  |_| 

****** Tool Name ::Ascii ART ******
       Why This tool :: This tool Is Made for TEXT TO ASCII ART
       Contact with Me : https://github.com/mrwnknown
    ** Donot try to Copy This. All right Reserved By MR.UNKOWN 

01. Ascii Art [Linux/windows]
02. Ascii Art [Windows]

''')

select = int(input("Choose the Number :"))

if(select == 1):
    type = str(input("Enter AnyThing:"))
    fonttype = str(input("Enter Your Faveourite Font:"))

    a = (pf.figlet_format(type, font = fonttype))

    print(a)

else:
    type = str(input("Enter AnyThing :: "))

    a = ((pf.figlet_format(type, font = 'big')))
    b = ((pf.figlet_format(type, font = '3-d')))
    e = ((pf.figlet_format(type, font = 'banner3-D')))
    f = ((pf.figlet_format(type, font = 'doh')))
    h = ((pf.figlet_format(type, font = 'letters')))
    j = ((pf.figlet_format(type, font = 'dotmatrix')))
    k = ((pf.figlet_format(type, font = 'bubble')))
    l = ((pf.figlet_format(type, font = 'bulbhead')))



    print(a)
    print(b)
    print(e)
    print(f)
    print(h)
    print(j)
    print(k)
    print(l)    
