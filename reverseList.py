def reverse(l):
    rev=l[::-1]
    print(rev)
def main():
    str = input("Enter a list separated by spaces ")
    strele = str.split(" ")
    l = []
    for x in strele:
        l.append(int(x))
    reverse(l)
main()
