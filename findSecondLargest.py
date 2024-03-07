def find_second_largest(l):
    largest=l[0]
    second_largest=l[0]
    for x in l:
        if (x>largest):
            second_largest=largest
            largest=x
        else:
            second_largest=max(second_largest,x)
    return second_largest
def main():
    s = input("Enter a list of elements separated by spaces : ")
    strEle = s.split(" ")
    l = [int(x) for x in strEle]
    secondlargest=find_second_largest(l)
    print("The largest element of the list  : ",secondlargest)

main()