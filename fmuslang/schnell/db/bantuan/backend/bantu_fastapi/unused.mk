--% /myfastapi/apps/product/__init__.py
--#

--% /myfastapi/apps/product/routes.py
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from apps.common.models import Message
import apps.product.models as schemas
import apps.product.crud as crud
from core.deps import get_db


router = APIRouter()


@router.get("", response_model=List[schemas.ProductResponse])
def read_products(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
  """
  GET list
  API_V1_STR: str = "__TEMPLATE_API_PREFIX"
  http://localhost:__TEMPLATE_SERVER_PORT____TEMPLATE_API_PREFIX/products
  """
  products = crud.product.get_multi(db, skip=skip, limit=limit)
  return products


@router.get("/{id}", response_model=schemas.ProductResponse)
def get_product(*, db: Session = Depends(get_db), id: int) -> Any:
  """
  GET detail
  http://localhost:__TEMPLATE_SERVER_PORT____TEMPLATE_API_PREFIX/products/:id
  """
  # products = crud.product.get(db, id)
  # return products
  product = crud.product.get(db, model_id=id)
  if not product:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"The product {id} not found.",
    )
  return product


@router.post("", response_model=schemas.ProductResponse)
def create_product(*, db: Session = Depends(get_db), product_in: schemas.ProductCreate) -> Any:
  """
  POST create
  http://localhost:__TEMPLATE_SERVER_PORT____TEMPLATE_API_PREFIX/products
  """
  product = crud.product.create(db, obj_in=product_in)
  return product


@router.put("", response_model=schemas.ProductResponse)
def update_product(*, db: Session = Depends(get_db), product_in: schemas.ProductUpdate) -> Any:
  """
  PUT update
  """
  product = crud.product.get(db, model_id=product_in.id)
  if not product:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="The product with this ID does not exist in the system.",
    )
  product = crud.product.update(db, db_obj=product, obj_in=product_in)
  return product


@router.delete("", response_model=Message)
def delete_product(*, db: Session = Depends(get_db), id: int) -> Any:
  """
  DELETE delete
  """
  product = crud.product.get(db, model_id=id)
  if not product:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="The product with this ID does not exist in the system.",
    )
  crud.product.remove(db, model_id=product.id)
  return {"message": f"Product with ID = {id} deleted."}

--#

--% /myfastapi/apps/product/crud.py
from typing import Optional, List

from sqlalchemy.orm import Session
from core.crud import CRUDBase
from .models import Product, ProductCreate, ProductUpdate


class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):
  # Declare model specific CRUD operation methods.
  pass


product = CRUDProduct(Product)
--#

--% /myfastapi/apps/product/models.py
from typing import Optional
from sqlalchemy import Column, Integer, String, Float
from pydantic import BaseModel
from core.db.base import Base


class Product(Base):
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False)
  price = Column(Float, nullable=False)
  
class ProductBase(BaseModel):
  id: Optional[int]
  name: Optional[str]
  price: Optional[float]

class ProductCreate(ProductBase):
  name: str
  price: float

class ProductUpdate(ProductBase):
  id: int
  pass

class ProductResponse(ProductBase):
  class Config:
    orm_mode = True

--#

