from datetime import datetime
from pydantic import BaseModel
from typing import Optional ,List



class team(BaseModel):
        id:int
        abbreviation:Optional[str]
        city:Optional[str]
        conference:Optional[str]
        division:Optional[str]
        full_name:Optional[str]
        name:Optional[str]
        error:Optional[str]
        class Config:
                orm_mode= True
        
class all_data(BaseModel):
        id:int
        first_name:Optional[str]
        last_name:Optional[str]
        position:Optional[str]
        team:Optional[List[team]]
        error:Optional[str]
        class Config:
                orm_mode= True
        
        
