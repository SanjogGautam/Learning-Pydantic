#pydantic is a data validationlibrary in python
#it is used by som of the top python modules like fastapi and langchain
#it allws usto bypass the issues of the the pydantic module
from pydantic import(BaseModel,ValidationError,model_validator)
class user(BaseModel):
    uid: int
    username: str
    email: str
    is_active: bool
    full_name: str | None=None #to give at least two names and giving a default value
user1=user(
    uid=1,
    username="Sanjog",
    email="gautamsanjok32@gmail.com",
    is_active=False
)
print(user)
print(user1)
#we can access the fields using (.) operator 
print(user1.username)
#models instances/objects are mutable by default
print(user1.uid)
#useful model methods
#1. converting model to a dictionary
b=user1.model_dump()
print(b)
#2. converting model to json
j=user1.model_dump_json(indent=4) #indent is used to make the json more readable
print(j)
#3. creating a model from a dictionary
data={
    "uid":2,
    "username":"Sanjog2",
    "email":"gsdfa",
    "is_active":True
}
user2=user.model_validate(data)
print(user2)
#4. creating a model from json
json_data='{"uid":3,"username":"Sanjog3","email":"gsdfa","is_active":true}'
user3=user.model_validate_json(json_data)
print(user3)