from fastapi import FastAPI
from routes.ask import router as ask_router
from routes.summarize import router as summarize_router
from routes.upload import router as upload_router

app = FastAPI()

# Register all routes
app.include_router(ask_router)
app.include_router(summarize_router)
app.include_router(upload_router)
