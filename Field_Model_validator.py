# custom validators in pydantic
from pydantic import (BaseModel, Field, field_validator,
                      ValidationError, model_validator,HttpUrl,ConfigDict)
#field validator is used to validate individual fields, while model validator is used to validate the entire model after all field validators have run.
class User(BaseModel):
    model_config=ConfigDict(populate_by_name=True)
    name: str = Field(..., min_length=3, max_length=50)
    age: int = Field(..., ge=0, le=120)
    website: HttpUrl = Field(..., description="User's personal website URL")# ... is to make it mandatory
    @field_validator('website',mode="before")
    def add_https(cls,value):
        if not value.startswith(("https://","http://")):
            return f"https://{value}"
        return value
    @field_validator('name')
    def validate_name(cls, value):
        if not value.isalpha():
            raise ValueError('Name must contain only letters')
        return value
    #field validator to check if age is at least 18 
    @field_validator('age')
    def validate_age(cls, value):
        if value < 18:
            raise ValueError('User must be at least 18 years old')
        return value
    # model-level validator to check the combination of name and age 
    #model validator checks the entire model after all field validators have run, allowing you to validate interdependent fields together.
    @model_validator(mode='before')
    def check_name_and_age(cls, values):
        name = values.get('name')
        age = values.get('age')
        if name and age and name.lower() == 'sanjog' and age < 20:
            raise ValueError('Sanjog must be at least 20 years old')
        return values
try:
    user = User(name='Sanjog', age=20,website="sanjoggautam.com.np")
except ValidationError as e:    
    print(e)
print(user.website.host)

