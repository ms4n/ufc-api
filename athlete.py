from bs4 import BeautifulSoup
import requests

athlete_url = 'https://www.ufc.com/athlete/{}'
gallery_url = 'https://www.ufc.com/gallery/photo-gallery-{}'


def athlete_slug(name):
    slug = name.lower().replace(' ', '-')
    return slug


def athlete_image(name):
    slug = athlete_slug(name)
    athlete_response = requests.get(athlete_url.format(slug))
    gallery_response = requests.get(gallery_url.format(slug))

    athlete_soup = BeautifulSoup(athlete_response.text, 'html.parser')
    gallery_soup = BeautifulSoup(gallery_response.text, 'html.parser')

    images = {}

    try:
        bio_image = athlete_soup.find('div', {'class': 'hero-profile__image-wrap'}).find('img')['src']
        images['bio_img'] = bio_image
    except AttributeError:
        images['bio_img'] = None

    try:
        main_image = gallery_soup.find('div', {'class': 'c-gallery-collapsed-item__content'}).find('source')['srcset']
        images['main_img'] = main_image
    except AttributeError:
        images['main_img'] = None

    return images
