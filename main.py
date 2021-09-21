from fastapi import FastAPI
from AthleteImage import athlete_image


app = FastAPI()


@app.get("/images/{athlete_name}")
def images(athlete_name: str):
    return athlete_image(athlete_name)


# if __name__ == '__main__':
#     import uvicorn
# uvicorn.run(app, host="127.0.0.1", port=8080)
