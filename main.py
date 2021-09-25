print("USEFUL INFO: in order to use this guide, you need to use the color code of the resistor. \n"
      "In other words, this guide won't work for potensiometers. \n"
      "The colors on the resistor should be red from left to right. \n"
      "If you don't know which direction you should begin from, \nthere are 2 telltale signs:\n"
      "1. If there is a gap between two of the outer colors, start from the opposite end.\n"
      "2. If one of the outermost colors is either gold or silver, start from the other end.\n"
      "When the program asks you about a color, write the three first letters of the color in\n"
      "non-capital letters. If the color is gray, write 'gra', in order to not confuse the computer\n"
      "into thinking it is green.\n"
      "Final note: the very last color of the row symbolizes the tolerance of the resistor, \n"
      "but I won't include that is this list as I don't know what it is.", 2 * "\n")


x = int(input("Are there 4 or 5 colored bands in total?\n"))

if x==4:
    a=input("What is the first color (first 3 letters)?\n")
    b=input("What is the second color (first 3 letters)?\n")
    c=input("What is the third color (first 3 letters)?\n")
    if a=="bla":
        a=0
    elif a=="bro":
        a=1
    elif a=="red":
        a=2
    elif a=="ora":
        a=3
    elif a=="yel":
        a=4
    elif a=="gre":
        a=5
    elif a=="blu":
        a=6
    elif a=="vio":
        a=7
    elif a=="pur":
        a=7
    elif a=="gra":
        a=8
    elif a=="whi":
        a=9
    if b=="bla":
        b=0
    elif b=="bro":
        b=1
    elif b=="red":
        b=2
    elif b=="ora":
        b=3
    elif b=="yel":
        b=4
    elif b=="gre":
        b=5
    elif b=="blu":
        b=6
    elif b=="vio":
        b=7
    elif b=="pur":
        b=7
    elif b=="gra":
        b=8
    elif b=="whi":
        b=9
    if c=="bla":
        print("\nThe resistor has a resistance of about",int(str(a) + str(b)) * 1, "ohm\nPress ctrl + F10 to try again")
    elif c=="bro":
        print("\nThe resistor has a resistance of about",int(str(a) + str(b)) * 10, "ohm\nPress ctrl + F10 to try again")
    elif c=="red":
        print("\nThe resistor has a resistance of about",int(str(a) + str(b)) * 100, "ohm\nPress ctrl + F10 to try again")
    elif c=="ora":
        print("\nThe resistor has a resistance of about",int(str(a) + str(b)) * 1_000, "ohm\nPress ctrl + F10 to try again")
    elif c=="yel":
        print("\nThe resistor has a resistance of about", int(str(a) + str(b)) * 10_000, "ohm\nPress ctrl + F10 to try again")
    elif c=="gre":
        print("\nThe resistor has a resistance of about", int(str(a) + str(b)) * 100_000, "ohm\nPress ctrl + F10 to try again")
    elif c=="blu":
        print("\nThe resistor has a resistance of about", int(str(a) + str(b)) * 1_000_000, "ohm\nPress ctrl + F10 to try again")
    elif c=="vio":
        print("\nThe resistor has a resistance of about", int(str(a) + str(b)) * 10_000_000, "ohm\nPress ctrl + F10 to try again")
    elif c=="pur":
        print("\nThe resistor has a resistance of about", int(str(a) + str(b)) * 10_000_000, "ohm\nPress ctrl + F10 to try again")
    elif c=="gra":
        print("\nThe resistor has a resistance of about", int(str(a) + str(b)) * 100_000_000, "ohm\nPress ctrl + F10 to try again")
    elif c=="whi":
        print("\nThe resistor has a resistance of about", int(str(a) + str(b)) * 1_000_000_000, "ohm\nPress ctrl + F10 to try again")
    elif c=="gol":
        print("\nThe resistor has a resistance of about", int(str(a) + str(b)) * 0.1, "ohm\nPress ctrl + F10 to try again")
    elif c=="sil":
        print("\nThe resistor has a resistance of about", int(str(a) + str(b)) * 0.01, "ohm\nPress ctrl + F10 to try again")
elif x==5:
    a = input("What is the first color (first 3 letters)?\n")
    b = input("What is the second color (first 3 letters)?\n")
    d=input("What is the third color (first 3 letters)?\n")
    c = input("What is the fourth color (first 3 letters)?\n")
    if a=="bla":
        a=0
    elif a=="bro":
        a=1
    elif a=="red":
        a=2
    elif a=="ora":
        a=3
    elif a=="yel":
        a=4
    elif a=="gre":
        a=5
    elif a=="blu":
        a=6
    elif a=="vio":
        a=7
    elif a=="pur":
        a=7
    elif a=="gra":
        a=8
    elif a=="whi":
        a=9
    if b=="bla":
        b=0
    elif b=="bro":
        b=1
    elif b=="red":
        b=2
    elif b=="ora":
        b=3
    elif b=="yel":
        b=4
    elif b=="gre":
        b=5
    elif b=="blu":
        b=6
    elif b=="vio":
        b=7
    elif b=="pur":
        b=7
    elif b=="gra":
        b=8
    elif b=="whi":
        b=9
    if d=="bla":
        d=0
    elif d=="bro":
        d=1
    elif d=="red":
        d=2
    elif d=="ora":
        d=3
    elif d=="yel":
        d=4
    elif d=="gre":
        d=5
    elif d=="blu":
        d=6
    elif d=="vio":
        d=7
    elif d=="pur":
        d=7
    elif d=="gra":
        d=8
    elif d=="whi":
        d=9
    if c=="bla":
        print("\nThe resistor has a resistance of about",int(str(a) + str(b)+str(d)) * 1, "ohm\nPress ctrl + F10 to try again")
    elif c=="bro":
        print("\nThe resistor has a resistance of about",int(str(a) + str(b)+str(d)) * 10, "ohm\nPress ctrl + F10 to try again")
    elif c=="red":
        print("\nThe resistor has a resistance of about",int(str(a) + str(b)+str(d)) * 100, "ohm\nPress ctrl + F10 to try again")
    elif c=="ora":
        print("\nThe resistor has a resistance of about",int(str(a) + str(b)+str(d)) * 1_000, "ohm\nPress ctrl + F10 to try again")
    elif c=="yel":
        print("\nThe resistor has a resistance of about", int(str(a) + str(b)+str(d)) * 10_000, "ohm\nPress ctrl + F10 to try again")
    elif c=="gre":
        print("\nThe resistor has a resistance of about", int(str(a) + str(b)+str(d)) * 100_000, "ohm\nPress ctrl + F10 to try again")
    elif c=="blu":
        print("\nThe resistor has a resistance of about", int(str(a) + str(b)+str(d)) * 1_000_000, "ohm\nPress ctrl + F10 to try again")
    elif c=="vio":
        print("\nThe resistor has a resistance of about", int(str(a) + str(b)+str(d)) * 10_000_000, "ohm\nPress ctrl + F10 to try again")
    elif c=="pur":
        print("\nThe resistor has a resistance of about", int(str(a) + str(b)+str(d)) * 10_000_000, "ohm\nPress ctrl + F10 to try again")
    elif c=="gra":
        print("\nThe resistor has a resistance of about", int(str(a) + str(b)+str(d)) * 100_000_000, "ohm\nPress ctrl + F10 to try again")
    elif c=="whi":
        print("\nThe resistor has a resistance of about", int(str(a) + str(b)+str(d)) * 1_000_000_000, "ohm\nPress ctrl + F10 to try again")
    elif c=="gol":
        print("\nThe resistor has a resistance of about", int(str(a) + str(b)+str(d)) * 0.1, "ohm\nPress ctrl + F10 to try again")
    elif c=="sil":
        print("\nThe resistor has a resistance of about", int(str(a) + str(b)+str(d)) * 0.01, "ohm\nPress ctrl + F10 to try again")







