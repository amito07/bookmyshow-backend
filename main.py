import logging
from fastapi import FastAPI
from mangum import Mangum
from routers import health_check, user_router

app = FastAPI()

log = logging.getLogger('uvicorn')



def create_application() -> FastAPI:
    _app = FastAPI(title="Restaurant Service", version="1.0.0")
    _app.include_router(health_check.router)
    _app.include_router(user_router.userRouter)
    return _app


app = create_application()
handler = Mangum(app)


@app.on_event("startup")
async def startup_event():
    log.info("Starting up....")

@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")