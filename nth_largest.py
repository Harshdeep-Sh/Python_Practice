# if k>length of array take modulus
# array does have duplicates
# can be or cannot be unsorted
arr=[2,4,6,7,3,5,2,5]
k=2
print(sorted(set(arr))[-k])