a =int(input("Enter the year :"))
if (a%4==0 or (a%100==0 and a%400==0)):
    print ("Leap year")
else:
    print ("Not a leap year")
