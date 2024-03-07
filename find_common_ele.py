def remove_duplicates(l1):
    unique=[]
    for x in l1:
        if x not in unique:
            unique.append(x)
    return unique
def find_common_elements(l1,l2):
    unique_l1=remove_duplicates(l1)
    unique_l2=remove_duplicates(l2)
    common_elements=[]
    for x in unique_l1:
        if x in unique_l2:
            common_elements.append(x)
    return common_elements

def main():
    s1=input("Enter a list 1 separated by space : ")
    string1=s1.split(" ")
    l1=[int(x) for x in string1]
    s2 = input("Enter a list 2 separated by space : ")
    string2 = s2.split(" ")
    l2 = [int(x) for x in string2]
    common_elements=find_common_elements(l1,l2)
    print("The common elements of list 1 and list 2 without duplicate elements are : ",common_elements)
main()