from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from athlete import athlete_image
from events import fetch_event_names

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/images/{athlete_name}")
def images(athlete_name: str):
    return athlete_image(athlete_name)


@app.get("/upcoming-events")
def upcoming_events():
    result = fetch_event_names()

    return result


# if __name__ == '__main__':
#     import uvicorn
# uvicorn.run(app, host="127.0.0.1")
