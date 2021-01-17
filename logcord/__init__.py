import hug

from logcord import routes


@hug.extend_api()
def add_routes() -> None:
    """Adds the routes for this app."""
    return [routes]
