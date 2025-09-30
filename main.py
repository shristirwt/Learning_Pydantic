# BaseModel is the core class in Pydantic that we inherit to create data models with automatic validation.
from pydantic import BaseModel

# We create a class Recipe that inherits BaseModel to get all the validation and serialization features from Pydantic
class Recipe(BaseModel):
    name:str
    description:str
    
# For now we are just printing it for the sake of learning only
def insert_recipe_data(recipe: Recipe):
    print(recipe.name)
    print(recipe.description)
    print("Inserted into database")

# A dictionary of recipe with key-value pairs
recipe_info={'name':'Shahi Paneer', 'description':'Shahi Paneer is a vegetarian Mughlai style curry where paneer is cooked in a creamy sauce made with onions, yogurt, nut and seeds'}

recipe1=Recipe(**recipe_info)
# ** operator unpacks the recipe_ifno dictionary and passes its key-value pairs as keyword arguments to the Recipe constructor

# recipe1=Recipe(**recipe_info) is equivalent to :
# recipe1=Recipe(name='Shahi Paneer', 'description'='Shahi Paneer is a vegetarian Mughlai style curry where paneer is cooked in a creamy sauce made with onions, yogurt, nut and seeds')

# Passing recipe1 into the function to insert it into database
insert_recipe_data(recipe1)