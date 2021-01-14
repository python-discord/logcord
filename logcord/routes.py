import hug
from falcon import HTTP_201, HTTP_422
from pydantic import ValidationError

from logcord.db import db
from logcord.utils import create_message_log


@hug.post('/api/message-logs', status=HTTP_201)
def post_message_log(body: hug.types.json, response: 'hug.Response') -> hug.types.json:
    """Creates a new message log from the given data."""
    try:
        log = create_message_log(body, db)
    except ValidationError:
        response.status = HTTP_422
    else:
        return {'log_id': log.id}
