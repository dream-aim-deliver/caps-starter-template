from typing import Generic, List, Optional, Literal, TypeVar
from pydantic import BaseModel

from lib.core.sdk.models import BaseSDKModel


TBaseSDKModel = TypeVar("TBaseSDKModel", bound=BaseSDKModel)


class BaseDTO(BaseModel, Generic[TBaseSDKModel]):
    """
    A base DTO class for the project

    @param status: The status of the operation, with True meaning 'success' and False meaning 'error'
    @type status: bool
    @param errorCode: The error code of the operation
    @type errorCode: Optional[int]
    @param errorMessage: The error message of the operation
    @type errorMessage: Optional[str]
    @param errorName: The error name of the operation
    @type errorName: Optional[str]
    @param errorType: The error type of the operation
    @type errorType: Literal["gateway_endpoint_error"] | Literal["database_error"] | str | None
    @param data: The data of the operation, representing a core entity
    @type data: Optional[TBaseModel]
    """

    status: bool
    errorCode: Optional[int] = None
    errorMessage: Optional[str] = None
    errorName: Optional[str] = None
    errorType: Literal["gateway_endpoint_error"] | Literal["database_error"] | str | None = None
    data: TBaseSDKModel | List[TBaseSDKModel] | None | List[None] = None


TBaseDTO = TypeVar("TBaseDTO", bound=BaseDTO[BaseSDKModel])
