import re

email = re.compile(r"^\S+@\S+\.\S+$")
string = str(input("Enter a valid email address: "))
password = re.compile(r"^[A-Z][a-z]+\d\d\W$")
str2 = input("Enter your password: ")

def validation(email,string):
    go_email = email.findall(string)
    return go_email
    

def pass_valid(password,str2):
    go_pass = password.findall(str2)
    return go_pass

def main():
    result = "".join(validation(email,string))
    print(result)
    result2 = "".join(pass_valid(password,str2))
    result_ano = len(result2) * "*"
    print(result_ano)

if __name__ == "__main__":
    main()
