from docxtpl import DocxTemplate
from pathlib import Path
from io import BytesIO

def generate_docx(template_path: Path, params: dict) -> BytesIO:
    """
    Генерация документа Word на основе шаблона и параметров.
    Возвращает объект BytesIO с готовым файлом.
    """
    doc = DocxTemplate(template_path)
    doc.render(params)

    # Сохраняем файл в памяти
    output = BytesIO()
    doc.save(output)
    output.seek(0)
    return output
