# Question 1

# Sample Input
# List = ['great','hello','hiyo','abc']
# Sample Output
# List = ['great', 'abc', 'hello','hiyo']

# Solution

n=int(input())
List=[]
for i in range(n):
    inp=input()
    List.append(inp)

#Sample Input for testing - Remove the comment below to test.
#List = ['great','hello','hiyo','abc']

List.sort(key= lambda List : List[-2])
print('Expected Output:',List)