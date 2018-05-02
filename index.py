# import json

from flask import Flask
from main_event import event_controller

app = Flask(__name__)

# TODO: add json schema


@app.route('/')
def index():
    '''Show all uploaded thumbnails in a big grid view
    '''
    # TODO: show the last 50 events in a grid(pics/video)
    # TODO: auto load more on scroll
    # TODO: scrollable nav bar on left that. each list element shows year/month going backward
    return 'Hello World!'


@app.route('/events', method='GET')
def get_events():
    '''Get pics/video events
    return: A list of event objects with pagination
    '''
    # TODO:get pagination fields
    offset = request.get('offset')
    start_date = request.get('start_date')

    if offset:
        events = event_controller.get_events(offset=offset)
    elif start_date:
        events = event_controller.get_events_starting_from(start_date)
    else:
        events = event_controller.get_most_recent_events()

    max_pages = event_controller.get_total_num_of_pages()
    return create_envelope(events, offset=offset, max_pages=max_pages)


@app.route('/event/:event_id', method='GET')
def get_event(event_id):
    event = event_controller.get_event_by_id(event_id)
    return create_envelope(event)


def create_envelope(json_obj, offset=None, max_pages=None):
    # TODO: get real envelope fields
    envelope = {
        'offset': 0 or offset,
        'max_pages': 0 or max,
    }
    return envelope.update(json_obj)
