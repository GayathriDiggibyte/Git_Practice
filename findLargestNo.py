def findLargest(l):
    largest=l[0]
    for x in l:
        if (x>largest):
            largest=x
    return largest

def main():
    s = input("Enter a list of elements separated by spaces : ")
    strEle = s.split(" ")
    l = [int(x) for x in strEle]
    largestno=findLargest(l)
    print("The largest element of the list  : ",largestno)

main()