import os
import uuid
from fastapi import UploadFile
from pathlib import Path

TEMP_DIR = Path("app/templates/")

def save_uploaded_file(file: UploadFile) -> str:
    """Сохраняет загруженный файл в временную директорию"""
    if not TEMP_DIR.exists():
        TEMP_DIR.mkdir(parents=True)
    file_id = f"{uuid.uuid4()}.docx"
    file_path = TEMP_DIR / file_id
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    return file_path
