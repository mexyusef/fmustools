from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from apps.common.models import Message
import apps.__TEMPLATE_TABLENAME_LOWER__.models as schemas
import apps.__TEMPLATE_TABLENAME_LOWER__.crud as crud
from core.deps import get_db


router = APIRouter()


@router.get("", response_model=List[schemas.__TEMPLATE_TABLENAME_CASE__Response])
def read___TEMPLATE_TABLENAME_LOWER__s(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
  """
  GET list
  API_V1_STR: str = "/api/v1"
  http://localhost:8000/api/v1/__TEMPLATE_TABLENAME_LOWER__s
  """
  __TEMPLATE_TABLENAME_LOWER__s = crud.__TEMPLATE_TABLENAME_LOWER__.get_multi(db, skip=skip, limit=limit)
  return __TEMPLATE_TABLENAME_LOWER__s


@router.get("/{id}", response_model=schemas.__TEMPLATE_TABLENAME_CASE__Response)
def get___TEMPLATE_TABLENAME_LOWER__(*, db: Session = Depends(get_db), id: int) -> Any:
  """
  GET detail
  http://localhost:8000/api/v1/__TEMPLATE_TABLENAME_LOWER__s/:id
  """
  # __TEMPLATE_TABLENAME_LOWER__s = crud.__TEMPLATE_TABLENAME_LOWER__.get(db, id)
  # return __TEMPLATE_TABLENAME_LOWER__s
  __TEMPLATE_TABLENAME_LOWER__ = crud.__TEMPLATE_TABLENAME_LOWER__.get(db, model_id=id)
  if not __TEMPLATE_TABLENAME_LOWER__:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"The __TEMPLATE_TABLENAME_LOWER__ {id} not found.",
    )
  return __TEMPLATE_TABLENAME_LOWER__


@router.post("", response_model=schemas.__TEMPLATE_TABLENAME_CASE__Response)
def create___TEMPLATE_TABLENAME_LOWER__(*, db: Session = Depends(get_db), __TEMPLATE_TABLENAME_LOWER___in: schemas.__TEMPLATE_TABLENAME_CASE__Create) -> Any:
  """
  POST create
  http://localhost:8000/api/v1/__TEMPLATE_TABLENAME_LOWER__s
  """
  __TEMPLATE_TABLENAME_LOWER__ = crud.__TEMPLATE_TABLENAME_LOWER__.create(db, obj_in=__TEMPLATE_TABLENAME_LOWER___in)
  return __TEMPLATE_TABLENAME_LOWER__


@router.put("", response_model=schemas.__TEMPLATE_TABLENAME_CASE__Response)
def update___TEMPLATE_TABLENAME_LOWER__(*, db: Session = Depends(get_db), __TEMPLATE_TABLENAME_LOWER___in: schemas.__TEMPLATE_TABLENAME_CASE__Update) -> Any:
  """
  PUT update
  """
  __TEMPLATE_TABLENAME_LOWER__ = crud.__TEMPLATE_TABLENAME_LOWER__.get(db, model_id=__TEMPLATE_TABLENAME_LOWER___in.id)
  if not __TEMPLATE_TABLENAME_LOWER__:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="The __TEMPLATE_TABLENAME_LOWER__ with this ID does not exist in the system.",
    )
  __TEMPLATE_TABLENAME_LOWER__ = crud.__TEMPLATE_TABLENAME_LOWER__.update(db, db_obj=__TEMPLATE_TABLENAME_LOWER__, obj_in=__TEMPLATE_TABLENAME_LOWER___in)
  return __TEMPLATE_TABLENAME_LOWER__


@router.delete("", response_model=Message)
def delete___TEMPLATE_TABLENAME_LOWER__(*, db: Session = Depends(get_db), id: int) -> Any:
  """
  DELETE delete
  """
  __TEMPLATE_TABLENAME_LOWER__ = crud.__TEMPLATE_TABLENAME_LOWER__.get(db, model_id=id)
  if not __TEMPLATE_TABLENAME_LOWER__:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="The __TEMPLATE_TABLENAME_LOWER__ with this ID does not exist in the system.",
    )
  crud.__TEMPLATE_TABLENAME_LOWER__.remove(db, model_id=__TEMPLATE_TABLENAME_LOWER__.id)
  return {"message": f"__TEMPLATE_TABLENAME_CASE__ with ID = {id} deleted."}

