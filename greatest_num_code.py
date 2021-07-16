print("Greatest of 4 nums")

var___1= int(input ("enter 1st num : "))
var___2= int(input ("enter 2nd num : "))
var___3= int(input ("enter 3rd num : "))
var___4= int(input ("enter 4th num : "))

if(var___2>var___4):
    f1=var___2
else:
    f1=var___4    

if(var___1>var___3):
    f2=var___1
else:
    f2=var___3

if(f1>f2):
    print("greatest num is ", f1)
else:
    print("greatest num is ", f2)