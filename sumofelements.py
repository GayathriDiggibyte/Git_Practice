def sumofelements(l):
    sum=0
    for i in range(len(l)):
        sum=sum+l[i]
    return sum
def reverse(l):
    print(reverse())
def main():
    a=input("Enter the elements of the list separated by space\n")
    ele=[]
    l=[]
    ele=a.split(" ")
    for i in range(len(ele)):
        l.append(int(ele[i]))
    res=sumofelements(l)
    print("The sum of the elements is : ",res)
    reverse(l)
main()

