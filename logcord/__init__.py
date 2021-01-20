import hug

from logcord.routes import api, frontend


@hug.extend_api()
def add_routes() -> None:
    """Adds the routes for this app."""
    return [api, frontend]
