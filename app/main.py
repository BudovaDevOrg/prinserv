from fastapi import FastAPI, UploadFile, Form, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from app.services import generate_docx
from app.utils import save_uploaded_file
from typing import Dict
import os

app = FastAPI()

class Params(BaseModel):
    params: Dict[str, str]

@app.post("/generate-docx/")
async def generate_docx_endpoint(template: UploadFile, params: str = Form(...)):
    """
    Генерация документа Word.
    - template: файл шаблона .docx
    - params: параметры для подстановки (строка JSON)
    """
    import json
    try:
        # Преобразование строки JSON в словарь
        params_dict = json.loads(params)

        # Сохранение загруженного шаблона
        template_path = save_uploaded_file(template)

        # Генерация документа
        generated_doc = generate_docx(template_path, params_dict)

        # Удаляем временный шаблон
        os.remove(template_path)

        # Возвращаем готовый файл
        return StreamingResponse(
            generated_doc,
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            headers={"Content-Disposition": f"attachment; filename=generated.docx"}
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка: {str(e)}")
