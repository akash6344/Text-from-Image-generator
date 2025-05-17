from fastapi import APIRouter
import easyocr

router = APIRouter()

@router.get("/text_from_image")
async def get_the_text():
    reader_obj = easyocr.Reader(['en'])
    # image_path = r"C:\Users\akash\Desktop\Resonate_Assignment\Task1\Text-from-Image-generator\assets\bloom_where_you_are.jpg"
    image_path = r"C:\Users\akash\Desktop\Resonate_Assignment\Task1\Text-from-Image-generator\assets\make_text_stand_out.jpeg"
    result = reader_obj.readtext(image_path)

    text_only = []

    for bbox,text,confidence in result:
        text_only.append(text)

    return {"text": text_only}
