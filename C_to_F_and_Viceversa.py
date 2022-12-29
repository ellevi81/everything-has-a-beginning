#Create a program that converts a given temperature in degrees Celsius to degrees Fahrenheit.
print ("---------------------------------------------------------------")
print (">>> hey i will help you converting C° to F° and viceversa!! <<<")
print ("---------------------------------------------------------------")
print ("                                                               ")


x = int(input("Write 1 for C° to F° --or-- 0 for F° to C°: "))

if x == 1:
    c = int(input("Write the temperature in F°: "))
    a = int(c*9/5)
    b = int(a + 32)
    print ("The temperature in Fahrenheit is: " + str(b) + "F°")

elif x == 0:
    d = int(input("Write the temperature in F°: "))
    s = int(d-32)
    r = int(s*5/9)
    print ("The temperature in Celsius is: " + str(r) + "C°")
