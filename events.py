from bs4 import BeautifulSoup
from bs4 import SoupStrainer as strainer
import requests
import cchardet
from athlete import athlete_bio_image

upcoming_events_url = "http://www.ufcstats.com/statistics/events/upcoming"
session = requests.Session()


def fetch_event_names():
    response = session.get(upcoming_events_url)
    soup = BeautifulSoup(response.text, 'lxml')
    events = soup.find_all('tr', {'class': 'b-statistics__table-row'})[2:]
    upcoming_events = []

    for event in events:
        event_name = event.find('a', {'class': 'b-link_style_black'}).text.strip()
        event_url = event.find('a', {'class': 'b-link_style_black'})['href'].strip()
        event_date = event.find('span', {'class': 'b-statistics__date'}).text.strip()
        event_venue = event.find('td', {'class': 'b-statistics__table-col_style_big-top-padding'}).text.strip()

        event_response = session.get(event_url)
        event_strainer = strainer('td', attrs={'class': 'b-fight-details__table-col l-page_align_left'})
        event_soup = BeautifulSoup(event_response.text, 'lxml', parse_only=event_strainer)

        fighter_name_1 = event_soup.find_all('a')[0].text.strip()
        fighter_name_2 = event_soup.find_all('a')[1].text.strip()

        fighter_1_img = athlete_bio_image(fighter_name_1)
        fighter_2_img = athlete_bio_image(fighter_name_2)

        events_dict = dict(zip(['name', 'url', 'date', 'venue', 'fighter_1', 'fighter_2'],
                               [event_name, event_url, event_date, event_venue, fighter_1_img, fighter_2_img]))
        upcoming_events.append(events_dict)

    return upcoming_events

