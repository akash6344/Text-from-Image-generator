from fastapi import FastAPI
from routes.OCR import router as ocr_router  # ✅ import the router object, not the function

app = FastAPI()

app.include_router(ocr_router, prefix="/api/OCR", tags=["OCR"])  # ✅ correct usage

@app.get("/")
def read_root():
    return {"message": "Welcome"}

