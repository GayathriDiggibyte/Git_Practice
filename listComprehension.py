def find_odd_elements(l):
    count_odd=[x for x in l if x%2 != 0]
    print("The odd elements : ",count_odd)

def find_even_elements(l):
    count_even=[x for x in l if x%2 == 0]
    print("The even elements : ",count_even)

def square_elements(l):
    square_list=[x**2 for x in l]
    print("The square of the individual elements  : ",square_list)
def main():
    s=input("Enter a list of elements separated by spaces : ")
    strEle=s.split(" ")
    l=[int(x) for x in strEle]
    find_odd_elements(l)
    find_even_elements(l)
    square_elements(l)
main()