b1=int(input("Input Your Marks in Bangla 1st Paper: "))
b2=int(input("Input Your Marks in Bangla 2nd Paper: "))
e1=int(input("Input Your Marks in English 1st Paper: "))
e2=int(input("Input Your Marks in English 2nd Paper: "))
math=int(input("Input Your Marks in Math: "))
Hmath=int(input("Input Your Marks in Higher Math Subject: "))
Hmathp=int(input("Input Your Marks in Higher Math Pratical: "))
bio=int(input("Input Your Marks in Biology Subject: "))
biop=int(input("Input Your Mark in Biology Pratical: "))
phy=int(input("Input Your Marks in Physics Subject: "))
phyp=int(input("Input Your Marks in Physics Pratical: "))
che=int(input("Input Your Marks in Chemistry Subject: "))
chep=int(input("Input Your Marks in Chemistry Pratical: "))
islam=int(input("Input Your Marks in Islam: "))
Sscince=int(input("Input Your Marks in Social Science: "))

#**********************************************************
#**********************************************************

totalbangla=b1+b2
totalEnglish=e1+e2
totalHmath=Hmath+Hmathp
totalBiology=bio+biop
totalPhysics=phy+phyp
totalChemistry=che+chep
#*********************************
#*********************************

Total=totalbangla+totalEnglish+totalHmath+totalChemistry+totalBiology+totalPhysics+math+islam+Sscince

avg=Total/9


#**************************
#**************************

print("*************************")
print("*************************")

print("Bangla 1st paper Grade is= ",b1)
print("Bangla 2nd paper Grade is= ",b2)
print("English 1st paper Grade is= ",e1)
print("English 2nd paper Grade is= ",e2)
print("Math Grade is= ",math)
print("Higher Math Subject Grade is= ",Hmath)
print("Higher Math Pratical Grade is= ",Hmathp)
print("Biology Subject Grade is= ",bio)
print("Biology Pratical Grade is= ",biop)
print("Physics Subject Grade is= ",phy)
print("Physics Pratical Grade is= ",phyp)
print("Chemistry Subject Grade is= ",che)
print("Chemistry Pratical Grade is= ",chep)
print("Islam Subject Grade is= ",islam)
print("Social Science Subject Grade is= ",Sscince)
print("*************************")
print("*************************")
print("Overall Bangla= ",totalbangla)
print("Overall English= ",totalEnglish)

#*****************************
#*****************************

print("**************************")
print("**************************")

if b1<33:
    print("You are Failed in Bangla 1st paper")
elif b2<33:
    print("You are Failed in Bangla 2nd paper")
elif e1<33:
    print("Your are Failed in English 1st paper")
elif e2<33:
    print("You are Failed in English 2nd paper")
elif math<33:
    print("You are failed in Math")
elif Hmath<24.75:
    print("You are failed in Higher math Subject")
elif Hmathp<8.25:
    print("You are Failed in Higher math Pratical")
elif bio<24.75:
    print("You are Failed in Biology Subject")
elif biop<8.25:
    print("You are Failed in Biology Pratical")
elif phy<24.75:
    print("You are Failed in Physics Subject")
elif phyp<8.25:
    print("You are Failed in Physics Pratical")
elif che<24.75:
    print("You are Failed in Chemistry Subject")
elif chep<8.25:
    print("You are Failed in Chemistry Pratical")
elif islam<33:
    print("You are Failed in Islam")
elif Sscince<33:
    print("You are Failed in Islam")
else:
    print("You are Pass")

print("**************************")
print("**************************")
if b1>33 and b2>33 and e1>33 and e2>33 and math>33 and Hmath>24.75 and Hmathp>8.25 and bio>24.75 and biop>8.25 and phy>24.75 and phyp>8.25 and che>24.75 and chep>8.25 and islam>33 and Sscince>33:

    if avg>80 and avg<100:
        print("Your Grade is A+")
    elif avg>70 and avg<79:
        print("Your Grade is A")
    elif avg>60 and avg<69:
        print("Your Grade Is A-")
    elif avg>50 and avg<59:
        print("Your Grade is B")
    elif avg>40 and avg<49:
        print("Your Grade is C")
    elif avg>33 and avg<39:
        print("Your Grade is D")
    elif avg<33:
        print("Your Grand is F")
    else:
        print("Invalid Grading")
else:
    print("Your are failed")

print("**************************")
print("**************************")
if b1>33 and b2>33 and e1>33 and e2>33 and math>33 and Hmath>24.75 and Hmathp>8.25 and bio>24.75 and biop>8.25 and phy>24.75 and phyp>8.25 and che>24.75 and chep>8.25 and islam>33 and Sscince>33:

    if avg>80 and avg<100:
        print("Your  Point is GPA- 5 ")
    elif avg>70 and avg<79:
        print("Your Point is GPA- 4" )
    elif avg>60 and avg<69:
        print("Your  Point is GPA- 3.5")
    elif avg>50 and avg<59:
        print("Your Point is GPA- 3 ")
    elif avg>40 and avg<49:
        print("Your Point is GPA- 2 ")
    elif avg>33 and avg<39:
        print("Your Point is GPA- 1 ")
    elif avg<33:
        print("Your Point is GPA- 0 ")
    else:
        print("Invalid Pointing")
else:
    print("Your Grade is GPA= 0.00 ")