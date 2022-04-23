

import subprocess
import uvicorn
import json_logging
from src import config
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import src.routes as routes
import src.storage.mongodb as database


app = FastAPI(title=config.PROJECT_NAME)

cors = config.Cors()

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors.origins,
    allow_credentials=True,
    allow_methods=cors.methods,
    allow_headers=cors.headers,
)


def init_structured_logging():
    json_logging.init_fastapi(enable_json=True)
    json_logging.init_request_instrument(app)


app.add_event_handler("startup", init_structured_logging)
app.add_event_handler("startup", database.connect)
app.add_event_handler("shutdown", database.close)


# ROUTES
routes.init(app)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    """catch http method data validation error"""
    err_list = []

    for err in exc.errors():
        key = err["loc"][1]
        msg = err["msg"]
        el = {key: msg}
        err_list.append(el)

    errors = {"errors": err_list}
    return JSONResponse(errors, status_code=400)


if __name__ == "__main__":
    if config.Env() == "dev":
        uvicorn.run("main:app", host="0.0.0.0", port=6000, reload=True)
    else:
        subprocess.call(["sh", "./start.sh"])
