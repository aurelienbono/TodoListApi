from pydantic import BaseModel
from typing import Optional

class TodoBase(BaseModel): 
    id : Optional[str] = str
    description: str 
    status :str 