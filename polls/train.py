# -*- coding: utf-8 -*-
class train:
    count=0
    kidscount=0
    adultcount=0
    seniorcount=0
    def main():
        a = int(input("Please enter ur age:"))
        global count
        count=count+1
        print("Total: ",str(count))
        return a 
    def kids():
        global kidscount
        kidscount=kidscount+1
        print("Kids: ",str(kidscount))
    def adult():
        global adultcount
        adultcount=adultcount+1
        print("Adults: ",str(adultcount))
    def seniorcitizen():
        global seniorcount
        seniorcount=seniorcount+1
        print("seniorcount: ",str(seniorcount))
    age = main()
        
    if age<18:kids()
    elif age>18 and age<60:adult()
    elif age>60: seniorcitizen()