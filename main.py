default = '\033[0m'
yellow= '\033[33m'
green= '\033[32m'
print(f"{green}Star Wars Name Generator{default}")
print()

FirstName= input("first name:").strip().capitalize()
print()
LastName = input("lastname:").strip().lower()
print()
MaidenName = input("mother's maiden name:").strip().capitalize()
print()
City = input("city where you were born:").strip().lower()
print()
print(f"""Your Star Wars Name is{yellow} {FirstName[:3]}{LastName[:3]} {MaidenName[:2]}{City[-3:]}{default}""")
print()
name= input(f"enter your first name, lastname, mother's maiden name and city where you were born").split()
print()
name = f"{FirstName} {LastName} {MaidenName} {City}".strip().title()
print()
print(name)