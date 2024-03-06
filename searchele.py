def searchEle(l,x):
    if x in l:
        print(x,"is present in the given list")
    else:
        print(x,"is not present in the given list")

def main():
    s=input("Enter a list of elements by spaces: ")

    strele=s.split(" ")
    l=[]
    for x in strele:
        l.append(int(x))
    x = int(input("Enter a element to be searched: "))
    searchEle(l,x)
main()