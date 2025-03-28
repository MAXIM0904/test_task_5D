import uvicorn
from fastapi import FastAPI

from api.routing_v1 import router_v1
from core.config import service_setting


app = FastAPI(
    title=service_setting.service_name,
    version="1.0.0",
    docs_url="/docs",
    contact={
        "name": service_setting.service_name
    },
    openapi_tags=[
        {
            "name": "Email",
            "description": "Отправка сообщений c помощью email address",
        },
        # {
        #     "name": "JWT",
        #     "description": "Отправка сообщений с помощью jwt token",
        # },
        {
            "name": "Task Scheduler",
            "description": "Планировщик отправки сообщений",
        },
    ],
)

app.include_router(router_v1, prefix="/v1")



if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=service_setting.host,
        port=service_setting.port,
        log_level="info"
    )
