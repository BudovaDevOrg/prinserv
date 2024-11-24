from fastapi import FastAPI, UploadFile, Form, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from app.services import generate_docx
from app.utils import save_uploaded_file
from typing import Dict
import os
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

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
        logger.debug("Received file: %s", template.filename)
        logger.debug("Received params: %s", params)

        # Преобразование строки JSON в словарь
        params_dict = json.loads(params)
        logger.debug("Parsed params_dict: %s", params_dict)

        # Сохранение загруженного шаблона
        template_path = save_uploaded_file(template)
        logger.debug("Template saved at: %s", template_path)

        # Генерация документа
        generated_doc = generate_docx(template_path, params_dict)
        logger.debug("Document generated successfully")

        # Удаляем временный шаблон
        os.remove(template_path)
        logger.debug("Temporary template file removed")

        # Возвращаем готовый файл
        return StreamingResponse(
            generated_doc,
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            headers={"Content-Disposition": f"attachment; filename=generated.docx"}
        )

    except Exception as e:
        logger.error("Error occurred: %s", str(e))
        raise HTTPException(status_code=500, detail=f"Ошибка: {str(e)}")
