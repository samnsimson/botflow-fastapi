from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import init_db
from routes.workflow_routes import router as workflow_router
# import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(root_path="/api/v1", version='v1', lifespan=lifespan)

# Routes
app.include_router(router=workflow_router, prefix='/workflow')

# if __name__ == '__main__':
#     uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)
