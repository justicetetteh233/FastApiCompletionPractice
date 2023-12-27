import routers
from fastapi import FastAPI
app  = FastAPI()


app.include_router(routers.app)



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
