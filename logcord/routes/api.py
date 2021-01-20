import hug
from falcon import HTTP_201, HTTP_404, HTTP_422
from pydantic import ValidationError

from logcord.db import db
from logcord.models import MessageLog
from logcord.utils import create_message_log


@hug.get('/api/message-logs')
def get_message_log(log_id: hug.types.text, response: 'hug.Response') -> hug.types.json:
    """Returns a message log from a given id."""
    log = db.message_logs.find_one({'id': log_id})

    if log is None:
        response.status = HTTP_404
    else:
        return MessageLog(**log).dict(by_alias=True)


@hug.post('/api/message-logs', status=HTTP_201)
def post_message_log(body: hug.types.json, response: 'hug.Response') -> hug.types.json:
    """Creates a new message log from the given data."""
    try:
        log = create_message_log(body, db)
    except ValidationError:
        response.status = HTTP_422
    else:
        return {'log_id': log.id}
