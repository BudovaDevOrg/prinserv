from pydantic import BaseModel
from typing import Dict

class DocxRequest(BaseModel):
    params: Dict[str, str]  # Параметры для подстановки в шаблон
