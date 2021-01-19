import os
from pathlib import Path

import hug
from jinja2 import Environment, PackageLoader, select_autoescape

if (LOGCORD_HOST := os.getenv('LOGCORD_HOST')) is None:
    raise RuntimeError('Missing `LOGCORD_HOST` environment variable..')

env = Environment(
    loader=PackageLoader('logcord', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

env.globals['PUBLIC_URL'] = LOGCORD_HOST


@hug.static('/static')
def static_files():
    """Serves static files for this app."""
    return [Path('logcord') / 'static']


@hug.get('/', output=hug.output_format.html)
def index():
    """Serves the homepage."""
    template = env.get_template('index.html')
    return template.render()
