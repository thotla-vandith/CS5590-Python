#Program to print alternate characters of a given string

def string_alternative(name):  #defining a function with name "string_alternative" with parameter as "name"
    print("Input: "+name)
    print("Output: "+name[::2])  #printing alternative elemenmts in the given string

string_alternative("Good Morning")  #calling the function

