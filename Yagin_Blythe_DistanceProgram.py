import math  
    
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

    
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

    
print(f"\nThe distance between the two points is: {distance:.2f}")


#Reflection
# Using a library is more practical than creating everything from scratch because it is faster and saves time. 
# When working from scratch, there is also a higher chance of making mistakes, while libraries are generally more reliable and can reduce errors.