from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Doctor chatbot backend is running"}