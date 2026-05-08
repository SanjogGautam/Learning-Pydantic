#pydantic is a data validationlibrary in python
#it is used by som of the top python modules like fastapi and langchain
#it allws usto bypass the issues of the the pydantic module
from pydantic import(BaseModel,ValidationError)
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
user1.uid="abc"
print(user1.uid)