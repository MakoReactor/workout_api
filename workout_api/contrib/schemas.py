from pydantic import BaseModel

class BaseSchema(BaseModel):
    class Copnfig:
        extra = 'forbid'
        from_atribuites = True