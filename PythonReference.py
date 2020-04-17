
#Conditional / Sequental Logic

x = 11

if x == 10 :
    print ("CONDITIONAL")
    print("SEQUENTAL")
if x < 10 :
    print("CONDITIONAL")
    print("SEQUENTIAL")


#ranges


for i in range (5) :
    x = x + 1
    print (x)
print("Done Incrementing x using range")


#elif


if x < 2 :
    print("SMALL")
elif x < 10 : #elif will exit the logic block if true
    print("MEDIUM")
elif x < 15 :
    print("LARGE")
else : #else is not required to use elif
    print ("EXTRA LARGE")
print("DONE JUDGING SIZE")

#try / except (used for accepting errors, often used with any user input)

astr = ("I'm a string!")
try :
    astr = int(astr) #cant convert a string to an integer
    print("All good, astr is string so the conversion is fine")
except: #catch `the error
    astr = -1
    print("Exception, error converting value to string. Still able to proceed because we caught it.")
print ("Done with try block")
print ("astr is ") + str(type(astr))

#math / type statement examples
calculationOne = 17//2
calculationTwo = 17/2.0
calculationThree = 12/3
calculationFour= 1 + 2 * 5
calculationFive = round(23.5662,2)


print (str(calculationOne), str(type(calculationOne)))
print (str(calculationTwo), str(type(calculationTwo)))
print (str(calculationThree), str(type(calculationThree)))
print (str(calculationFour), str(type(calculationFour)))
print (str(calculationFive), str(type(calculationFive)))
