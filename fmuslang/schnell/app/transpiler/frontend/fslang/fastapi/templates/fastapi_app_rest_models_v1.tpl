from typing import Optional
from sqlalchemy import (
  Column, 
  Boolean, 
  DateTime, 
  Float,
  ForeignKey,
  Integer, 
  String, 
  Text,  
)
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from core.db.base import Base


class __TEMPLATE_TABLENAME_CASE__(Base):
  #id = Column(Integer, autoincrement=True, primary_key=True, index=True)
__TEMPLATE_MODEL_SQLAL_FIELDS__
  
class __TEMPLATE_TABLENAME_CASE__Base(BaseModel):
  #id: Optional[int]
__TEMPLATE_BASEMODEL_OPTIONAL_FIELDS__

class __TEMPLATE_TABLENAME_CASE__Create(__TEMPLATE_TABLENAME_CASE__Base):
__TEMPLATE_BASEMODEL_FIELDS__

class __TEMPLATE_TABLENAME_CASE__Update(__TEMPLATE_TABLENAME_CASE__Base):
  id: int
  pass

class __TEMPLATE_TABLENAME_CASE__Response(__TEMPLATE_TABLENAME_CASE__Base):
  class Config:
    orm_mode = True
