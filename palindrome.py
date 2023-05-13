n=int(input("ENTER THE NUMBER "))
def palindrome(x):
    st=str(x)
    rst=st[::-1]
    if st==rst:
        print("YES")
    else:
        print("NO")
palindrome(n)

    