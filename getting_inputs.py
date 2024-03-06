def display_input(number,string_val,float_val,bool_val,complex_val):
    print("The integer value is : ",number,type(number))
    print("The string value is : ",string_val,type(string_val))
    print("The float value is : ",float_val,type(float_val))
    print("The boolean value is : ",bool_val,type(bool_val))
    print("The complex number : ",complex_val)

def getting_input():
    number=int(input("Enter a number: "))
    string_val=input("Enter a string: ")
    float_val=float(input("Enter a decimal number: "))
    bool_val=bool(input("Enter a boolean value: "))
    complex_val=complex(input("Enter a complex number: "))
    display_input(number,string_val,float_val,bool_val,complex_val)

getting_input()

