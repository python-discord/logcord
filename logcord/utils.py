import secrets

from pymongo.database import Database

from logcord.models import MessageLog


def create_message_log(log_data: dict, db: Database) -> MessageLog:
    """
    Creates and saves a message log from the given data.

    An ID is automatically generated for the log.
    """
    while True:
        log_id = secrets.token_urlsafe(9)

        if db.message_logs.find_one({'id': log_id}) is None:
            break

    log = MessageLog(id=log_id, **log_data)
    db.message_logs.insert(log.dict(by_alias=True))

    return log
