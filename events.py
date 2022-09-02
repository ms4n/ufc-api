from bs4 import BeautifulSoup
import requests
from athlete import athlete_image


upcoming_events_url = "http://www.ufcstats.com/statistics/events/upcoming"


def fetch_event_names():
    response = requests.get(upcoming_events_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    events = soup.find_all('tr', {'class': 'b-statistics__table-row'})[2:]
    upcoming_events = []

    for event in events:
        event_name = event.find('a', {'class': 'b-link_style_black'}).text.strip()
        event_url = event.find('a', {'class': 'b-link_style_black'})['href'].strip()
        event_date = event.find('span', {'class': 'b-statistics__date'}).text.strip()
        event_venue = event.find('td', {'class': 'b-statistics__table-col_style_big-top-padding'}).text.strip()

        event_response = requests.get(event_url)
        event_soup = BeautifulSoup(event_response.text, 'html.parser')

        fighter_name_1 = event_soup.find_all('a', {'class': 'b-link'})[0].text.strip()
        fighter_name_2 = event_soup.find_all('a', {'class': 'b-link'})[1].text.strip()

        fighter_1_img = athlete_image(fighter_name_1)['bio_img']
        fighter_2_img = athlete_image(fighter_name_2)['bio_img']

        events_dict = dict(zip(['name', 'url', 'date', 'venue', 'fighter_1', 'fighter_2'],
                               [event_name, event_url, event_date, event_venue, fighter_1_img, fighter_2_img]))
        upcoming_events.append(events_dict)

    return upcoming_events

# fetch_event_names()
