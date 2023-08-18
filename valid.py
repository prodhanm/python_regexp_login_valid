import re

email = re.compile(r"^\S+@\S+\.\S+$")
string = str(input("Enter a valid email address: "))

def validation(email,string):
    go_email = email.findall(string)
    return go_email
    
def main():
    result = "".join(validation(email,string))
    print(result)

if __name__ == "__main__":
    main()
