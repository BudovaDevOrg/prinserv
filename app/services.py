from docxtpl import DocxTemplate
from pathlib import Path
from io import BytesIO
import logging

# Setup logging
logger = logging.getLogger(__name__)

def generate_docx(template_path: Path, params: dict) -> BytesIO:
    """
    Генерация документа Word на основе шаблона и параметров.
    Возвращает объект BytesIO с готовым файлом.
    """
    logger.debug("Generating document using template: %s", template_path)
    logger.debug("Parameters for rendering: %s", params)

    try:
        doc = DocxTemplate(template_path)
        doc.render(params)
        logger.debug("Template rendered successfully")

        # Сохраняем файл в памяти
        output = BytesIO()
        doc.save(output)
        output.seek(0)
        logger.debug("Document saved in memory")
        return output
    except Exception as e:
        logger.error("Error during document generation: %s", str(e))
        raise
