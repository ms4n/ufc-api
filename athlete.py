from bs4 import BeautifulSoup as soup
from bs4 import SoupStrainer as strainer
import requests
import cchardet

athlete_url = 'https://www.ufc.com/athlete/{}'


def athlete_slug(name):
    slug = name.lower().replace(' ', '-')
    return slug


def athlete_bio_image(name):
    slug = athlete_slug(name)
    athlete_response = requests.get(athlete_url.format(slug))

    bio_img_strainer = strainer('div', attrs={'class': 'hero-profile__image-wrap'})
    athlete_soup = soup(athlete_response.text, 'lxml', parse_only=bio_img_strainer)

    try:
        bio_image = athlete_soup.find('img')['src']
    except AttributeError:
        bio_image = None

    return bio_image

# print(athlete_bio_image('conor mcgregor'))
