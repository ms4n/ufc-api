from fastapi import FastAPI
from athlete import athlete_image
from events import fetch_event_name

app = FastAPI()


@app.get("/images/{athlete_name}")
def images(athlete_name: str):
    return athlete_image(athlete_name)


@app.get("/upcoming-events")
def upcoming_events():
    result = fetch_event_name()

    return result


# if __name__ == '__main__':
#     import uvicorn
# uvicorn.run(app, host="127.0.0.1")
