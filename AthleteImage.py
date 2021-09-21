from bs4 import BeautifulSoup
import requests
import json

athlete_url = 'https://www.ufc.com/athlete/{}'


def athlete_slug(name):
    slug = name.lower().replace(' ', '-')
    return slug


def athlete_image(name):
    slug = athlete_slug(name)
    response = requests.get(athlete_url.format(slug))
    soup = BeautifulSoup(response.text, 'html.parser')
    images = {'hero_image': soup.find('div', {'class': 'c-hero--full'}).find('img')['src'],
              'bio_image': soup.find('div', {'class': 'c-bio__image'}).find('img')['src'],
              'card_image_1': soup.find('div', {'class': 'c-mat__image-1'}).find('img')['src'],
              'card_image_2': soup.find('div', {'class': 'c-mat__image-2'}).find('img')['src'],
              }
    return images
