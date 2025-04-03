from fastapi import FastAPI
app = FastAPI()
from app.config.db import engine
from app.routes import router
@app.get("/api/v1/auth")
def root():
    return {"message": "Welcome to the Auth Service API"}

app.include_router(router,prefix='/api/v1')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5001)

