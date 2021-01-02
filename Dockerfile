FROM python:3.9-slim

# Set pip to have cleaner logs and no saved cache
ENV PIP_NO_CACHE_DIR=false \
    PIPENV_HIDE_EMOJIS=1 \
    PIPENV_IGNORE_VIRTUALENVS=1 \
    PIPENV_NOSPIN=1

# Install pipenv
RUN pip install -U pipenv

# Create the working directory
WORKDIR /app

# Install project dependencies
COPY Pipfile* ./
RUN pipenv install --system --deploy

# Install gunicorn
RUN pip install -U gunicorn

# Copy the source code in last to optimize rebuilding the image
COPY . .

ENTRYPOINT ["gunicorn"]
CMD ["-w", "4", "-b", "0.0.0.0:8000", "logcord:__hug_wsgi__"]
