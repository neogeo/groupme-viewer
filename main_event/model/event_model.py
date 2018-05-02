def s3_obj_to_event(s3_obj):

    event = {
        'date': s3_obj.date,
        'size': s3_obj.size,
        'type': get_s3_obj_type(s3_obj),
        'width': s3_obj.width,
        'height': s3_obj.height,
    }

    return event


def get_s3_obj_type(s3_obj):
    if s3_obj.type == 'img':
        return 'img/jpeg'
    elif s3_obj.type == 'video':
        return 'vid/mp4'
    else:
        raise Exception('unsupported type')
