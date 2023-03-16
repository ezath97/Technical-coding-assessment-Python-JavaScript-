# Question 2

#Your task is to complete the validate_triangle and validate_rectangle functions for the classes. Hint for validating is given in the
#comments of the code. Also you will have to print the following after validation in respective functions:-

# 1.Invalid Triangle: If the triangle sum property of sides is not valid(More hint in the comments of code)
# 2.Valid Triangle: If the triangle sum property of sides is valid.
# 3.Valid Rectangle: If 2 side pairs are same and they are input in correct order like l,b,l,b
# 4.Invalid Rectangle: If Not Valid rectangle as stated above.


# Solutions

T1,T2,T3=map(int,input().split())
R1,R2,R3,R4=map(int,input().split())


#Sample Input for testing - Remove the comment below to test.
#T1,T2,T3 = 3,4,5
#R1,R2,R3,R4 = 2,4,2,4

def validate_triangle(a,b,c):
    if (a+b > c) and (a+c > b) and (c+b > a):
        return('Valid Triangle')
    else:
        return('Invalid Triangle')
    
def validate_rectangle(l1,b1,l2,b2):
    if (l1 == l2) and (b1 == b2):   
        return('Valid Rectangle')
    else:
        return('Invalid Rectangle')
    

print(validate_triangle(T1,T2,T3))    
print(validate_rectangle(R1,R2,R3,R4))