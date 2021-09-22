from bs4 import BeautifulSoup
import requests

upcoming_events_url = "http://www.ufcstats.com/statistics/events/upcoming"


def fetch_event_name():
    response = requests.get(upcoming_events_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    events = soup.find_all('a', {'class': 'b-link b-link_style_black'})
    upcoming_events = []

    for event in events:
        events_dict = dict(zip(['name', 'url'], [event.text.strip(), event['href'].strip()]))
        upcoming_events.append(events_dict)

    return upcoming_events
