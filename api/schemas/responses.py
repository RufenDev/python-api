from pydantic import BaseModel
from typing import Literal, Optional, Any

class BasicResponse[DataT](BaseModel):
    result: Literal["OK", "ERROR", "WARNING"] = "OK"
    message: Optional[str] = None
    data: Optional[DataT | Any] = None
