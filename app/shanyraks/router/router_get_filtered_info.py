from datetime import datetime
from typing import Any, List

from fastapi import Depends, Response, APIRouter
from pydantic import Field
from fastapi.responses import JSONResponse

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel

from ..service import Service, get_service
from . import router


# class GetFilteredInfoRequest(AppModel):
#     id: Any = Field(alias="_id")
#     limit: int
#     offset: int
#     type: str
#     area: float
#     rooms_count: int
#     price_from: int
#     price_until: int

# class GetFilteredInfoResponse(AppModel):
#     total: int
#     limit: int
#     offset: int
#     type: str
#     area: float
#     rooms_count: int
#     price_from: str
#     price_until: Any
     
# class ShanyrakData(AppModel):
#     _id: str
#     type: str
#     price: int
#     address: str
#     area: float
#     rooms_count: int
#     location: dict


# class GetFilteredInfoResponse(AppModel):
#     total: int
#     objects: List[ShanyrakData]

# router = APIRouter()

# @router.get("/all", response_model=GetFilteredInfoResponse)
# def get_filtered_info(
#     input: GetFilteredInfoRequest,
#     svc: Service = Depends(get_service),
# ) -> JSONResponse:
#     result = svc.repository.get_filtered_info(GetFilteredInfoRequest)
#     return JSONResponse(content=GetFilteredInfoResponse.dict(), status_code=200)

class Post(AppModel):
    address: str
    price: int
    type: str
    rooms_count: int


class GetFilteredInfoResponse(AppModel):
    total: int
    objects: List[Post]

@router.get("/", response_model=GetFilteredInfoResponse)
def  get_filtered_info(
    limit: int,
    offset: int,
    svc: Service = Depends(get_service),
):
    result = svc.repository.get_filtered_info(limit, offset)
    return {
        "total" : len(result),
        "objects" : result
    }
