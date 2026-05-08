from pydantic import(BaseModel,ValidationError,model_validator,EmailStr,Field)
from typing import Annotated,Literal
from datetime import datetime
#annoted is the wayto add metadata to a field and literal is used to restrict the values of a field to a specific set of values.
#field is used to add metadata to a field and also to set default values and validators for a field
b=Annotated[
        Literal["admin", "user", "guest"],
        Field(default="user")] #this will only allow the values "admin","user","guest" for the role field
    #combine Field and Annotated to create a field with both metadata and validation
class user(BaseModel):
    uid: int=Field(alias="user_id") #this will allow us to use the alias "user_id" instead of "uid" when creating a user object
    username: str
    date_of_birth: datetime=Field(default_factory=lambda:datetime.now()) #this will set the default value of date_of_birth to the current date and time lambda is used to create a default value that is evaluated at runtime
    email: EmailStr
    is_active: bool
    full_name: str | None=None #to give at least two names and giving a default value
    age:int=Field(gt=0,lt=150) #this will only allow the values between 0 and 150 for the age field
    role: b


    status: Annotated[
        Literal["active", "inactive"],
        Field(default="active")
    ]
    #we can also use Field to set default values for the fields and and also to set validators for the fields
    #annotated is more flexible than field because it can be used with any type of field, whereas field can only be used with pydantic fields like int, str, bool etc.
try:
    user1=user(
        user_id=1,
        username="Sanjog",
        email="gautam@gmail.com",
        is_active=False,
        age=25,
        role="admin",
        status="active"
    )
except ValidationError as e:
    print(e)
print(user1.model_dump_json(indent=1))

