'''Prepare a python application for the following.
 Read a string of length 9 
 Find median character.
 Calculate the sum of ASCII values of all the characters in the string before 
and after the median character excluding the median character. 
 Print the max value'''
'''
def median_char(s):
    median_char = s[4] #4th character is median of a 9 length string
    print(median_char)

def max_ascii(s):
    l_sum=0
    r_sum=0
    for i in range(0,4):
        l_sum += ord(s[i]) #store ascii sum of left side characters(index 0 to 3)
    for j in range(5,9):
        r_sum += ord(s[j]) #store ascii sum of right side characters(index 5 to 9)
    print(max(l_sum,r_sum))
    print("l_sum: ",l_sum)
    print("r_sum: ",r_sum)

s = input("Enter string: ")
if(len(s)>=9):
    s = s[:9] #slicing the first 9 characters of string
    print(s)
    median_char(s)
    max_ascii(s)
else:
    print("String is too short")

'''
'''
Prepare a python application for the following.
 Create a list that contains at least one int,float,list,tuple, and string
 Print the type of every element in the list with its size and memory locations'''
'''
import sys
Main_list = [22,3.0,['l','i','s','t'],('t','u','p','l','e'),"String"]
for i in Main_list:
    print(i)
    print("Type: ",type(i))
    print("Size: ",sys.getsizeof(i))
    print("Memory Location: ",id(i))
'''

'''Prepare a python application for the following.
 Select a random value in the range of 
 Check that x==y. If true, print 1 else print 0.
 Loop through the above steps for 100 iterations and find the total
occurrences of 1 and 0 & print the same'''
'''
import numpy as np
count_equal = 0
count_notEqual = 0
for i in range(100):
    x = np.random.randint(0,100)
    y = np.random.randint(0,100)
    if(x==y):
        print("1")
        count_equal+=1
    else:
        print("0")
        count_notEqual+=1

print("1 occurrrences: ",count_equal)
print("0 occurrrences: ",count_notEqual)
'''
'''

print("Enter name of the file")
fileName= str(input())
fileHandle= open(fileName,"r")
tot = 0
vowels = ['a','e','i','o','u','A','E','I','O','U']

for char in fileHandle.read():
    if char in vowels:
        tot+=1
fileHandle.close()

print("Total number of vowels are: ",tot)
'''
'''

print("Enter name of the file")
fileName= str(input())
fileHandle= open(fileName,"r")
st = fileHandle.read()
lst = st.split()
cd=[]
for i in lst:
    l = len(i)
    if l in cd:
        continue
    else:
        cd.append(l)

print(len(cd))
'''

st = "file handles pythons program "
lst = st.split()
cd=[]
for i in lst:
    l = len(i)
    if l in cd:
        continue
    else:
        cd.append(l)

print(len(cd))






























