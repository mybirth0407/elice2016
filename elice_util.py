# -*- coding: utf-8 -*-

import base64 as _base64
import fcntl as _fcntl
import mimetypes as _mimetypes
import os.path as _ospath
import struct as _struct

_EventType = {
    'text': 200,
    'image': 210,
    'file': 220,
    'html': 230
}

try:
    # PY2
    _str_type = (str, unicode)
    _bin_type = str
except NameError:
    # PY3
    _str_type = str
    _bin_type = bytes


def _send_to_elice(event_type, event_data):
    if event_type not in _EventType:
        raise ValueError('Unexpected event type: %s' % event_type)

    if not isinstance(event_data, _bin_type):
        raise TypeError('event_data should be a bytes')

    event_size = len(event_data)

    event_header = _struct.pack('>BxxxL', _EventType[event_type], event_size)

    with open('/tmp/elice_out.lock', 'w') as lock_f:
        # send event header and data atomically
        _fcntl.flock(lock_f, _fcntl.LOCK_EX)

        with open('/dev/elice_out', 'wb') as f:
            f.write(event_header)
            f.write(event_data)


def send_image(img_file_or_path, fallback_image_type='png'):
    '''Send a image file to elice

    The function will guess image format based on filename but it might fail to guess.
    In that situation, the function assume image type as according to `fallback_image_type` parameter.

    Supporting image type : png, jpg, jpeg, gif, bmp

    Usage

    >> with open('sample.png') as img_file:
        elice_utils.send_image(img_file)

    or

    >> elice_utils.send_image('some_image', 'jpg')

    '''
    _SUPPORTING_IMAGE_TYPES = ['png', 'jpg', 'jpeg', 'gif', 'bmp', 'svg']

    if isinstance(img_file_or_path, _str_type):
        img_file = open(img_file_or_path, 'rb')

        filename = _ospath.basename(img_file_or_path)
    else:
        img_file = img_file_or_path
        if not hasattr(img_file, 'read') or not callable(img_file.read):
            raise TypeError('image_file has no callable read method')

        if hasattr(img_file, 'name'):
            filename = _ospath.basename(img_file.name)
        else:
            filename = ''

    if fallback_image_type not in _SUPPORTING_IMAGE_TYPES:
        raise ValueError('Not supported fallback image type: %s' % image_type)

    image_type = filename.split('.')[-1]

    if image_type not in _SUPPORTING_IMAGE_TYPES:
        image_type = fallback_image_type

    mimetype = _mimetypes.types_map.get('.%s' % image_type, 'image/%s' % image_type)

    data_uri_header = 'data:%s;base64,' % mimetype
    data_uri_header = data_uri_header.encode('utf-8')

    data_uri_content = _base64.b64encode(img_file.read())

    _send_to_elice('image', data_uri_header + data_uri_content)


def send_file(a_file_or_path):
    '''Send a file to elice

    Usage

    >> with open('result.xls') as a_file:
        elice_utils.send_file(a_file)

    or

    >> elice_utils.send_file('result.xls')

    '''
    if isinstance(a_file_or_path, _str_type):
        a_file = open(a_file_or_path, 'rb')

        filename = _ospath.basename(a_file_or_path)
    else:
        a_file = a_file_or_path
        if not hasattr(a_file, 'read') or not callable(a_file.read):
            raise TypeError('a_file has no callable read method')

        if not hasattr(a_file, 'name'):
            raise TypeError('a_file has no name attribute')

        filename = _ospath.basename(a_file.name)

    mimetype, _ = _mimetypes.guess_type(filename)
    mimetype = mimetype if mimetype else 'application/octet-stream'

    data_uri_header = '%s;data:%s;base64,' % (filename, mimetype)
    data_uri_header = data_uri_header.encode('utf-8')

    data_uri_content = _base64.b64encode(a_file.read())

    _send_to_elice('file', data_uri_header + data_uri_content)

def visualize(X, Y, results):
    import matplotlib as mpl
    mpl.use("Agg")
    import matplotlib.pyplot as plt
    import numpy

    slope = results.params[1]
    intercept = results.params[0]

    plt.scatter(X, Y)
    reg_line_x = numpy.array([min(X), max(X)])
    reg_line_y = reg_line_x * slope + intercept
    plt.plot(reg_line_x, reg_line_y, color='r')

    plt.savefig("image.svg", format="svg")
    send_image("image.svg")
