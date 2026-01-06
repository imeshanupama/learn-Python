print("Hello, Python!")

name="Imesh"
age=27  
print(f"My name is {name} and I am {age} years old.")

birth_country="Sri Lanka"
print("I was born in " + birth_country)
current_country1="Germany"
print("Now I live in " + current_country1)

next_year_age=age+1
print(f"Next year, I will be {next_year_age} years old.")

my_hobbies=["Reading", "Traveling", "Coding"]
print("My hobbies are:")
for hobby in my_hobbies:
    print("- " + hobby)

favorite_language="Python"
print(f"My favorite programming language is {favorite_language}.")  
print("I love learning new programming languages!")

my_ambition="to become a proficient software developer"
print(f"My ambition is {my_ambition}.")

education_level="Abitur"    
print(f"My highest education level is {education_level}.")  
bachelor_degree="Studying Sustainable Business and Law In Umwelt Campus Birkenfeld"
print(f"I am currently {bachelor_degree}.")
I_want_to_join="I want to join for a Ausbildung as Fachinformatiker for Systemintegration or Facinformatiker for APP Development."
print(I_want_to_join)

def check_age(age):
    if age < 18:
        return "You are a minor."
    else:
        return "You are an adult."
age_status = check_age(age)
print(age_status)

def check_age(age):
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")
check_age(age)

def greet(name):
    print(f"Hello, {name}!")
greet(name)

birth_date="25th february" 
print(f"My birth date is {birth_date}.")

def calculate_birth_year(current_year, age):
    print(f"My birth year is {current_year - age}.")
calculate_birth_year(2024, age)

def greet(name):
    print(f"Hello, {name}! Welcome to Python.")

greet("Imesh")
greet("Alex")
greet("Maria")

friends=["Alex", "Maria", "John"]
for friend in friends:
    greet(friend)

user_name=input("Enter your name: ")
greet(user_name)

age=input("Enter your age: ")

user_age=int(input("Enter your age: "))

if user_age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


