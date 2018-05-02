import arrow
import math

from model import event_model

DEFAULT_BATCH_SIZE = 50


def get_events(offset=0):
    '''Get a group of the first events
    offset: Optional offset from the first event
    '''
    events = []
    for num, s3_obj in enumerate(1, s3_helper.get_sorted_objects(offset)):
        if num >= DEFAULT_BATCH_SIZE:
            break

        event = event_model.s3_obj_to_event(s3_obj)
        events.append(event)

    return events


def get_events_starting_from(start_date, offset=0):
    '''Get the last N events starting a given date
    '''
    events = []
    for num, s3_obj in enumerate(1, s3_helper.get_sorted_objects(start_date, offset)):
        if num >= DEFAULT_BATCH_SIZE:
            break

        event = event_model.s3_obj_to_event(s3_obj)

    return events


def get_most_recent_events():
    start_date = arrow.now()

    events = []
    for num, s3_obj in enumerate(1, s3_helper.get_sorted_objects(start_date, offset)):
        if num >= DEFAULT_BATCH_SIZE:
            break

        event = event_model.s3_obj_to_event(s3_obj)

    return events


def get_event_by_id(event_id):
    s3_helper.get_event_by_metadata_id(event_id)

    event = event_model.s3_obj_to_event(s3_obj)

    return events


def get_total_num_of_pages()
    return math.ceil(maths3_helper.total_object_count()/DEFAULT_BATCH_SIZE)

