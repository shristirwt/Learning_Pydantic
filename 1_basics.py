# BaseModel is the core class in Pydantic that we inherit to create data models with automatic validation.
from pydantic import BaseModel

# We create a class Recipe that inherits BaseModel to get all the validation and serialization features from Pydantic
class UserProfile(BaseModel):
    name:str
    age:int
    
# For now we are just printing it for the sake of learning only
def insert_recipe_data(user: UserProfile):
    print(user.name)
    print(user.age)
    print("Inserted into database")

# A dictionary of user_info with key-value pairs
user_info={'name':'Ajay Gupta', 'age':30}

user1=UserProfile(**user_info)
# ** operator unpacks the user_info dictionary and passes its key-value pairs as keyword arguments to the UserProfile constructor

# user1=UserProfile(**user_info) is equivalent to :
# user_info=UserProfile('name':'Ajay Gupta', 'age':30)

# Passing user1 into the function to insert it into database
insert_recipe_data(user1)














I am student at Graphic Era University, Dehradun
I am pursuing BTech CSE (AI & DS)
My top skills are C, C++, Java, Python, ML fundamentals, Pydantic
My favorite repo in which I have been a maintainer also is RecodeHive/Stackoverflow-Analysis

Nowadays, I am focusing on DSA, building my resume by building projects
Linkedin: www.linkedin.com/in/shristirawat
twitter: @ShristiRawat137

I want a professional theme
I have achieved AWS Solutions Architechture Job Simulation certificate on Forage

