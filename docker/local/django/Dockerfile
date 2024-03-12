# Use the specified Python version as an argument
ARG PYTHON=3.10.4-bullseye
FROM python:${PYTHON} as python

# Set the build stage
FROM python as python-build-stage
ARG BUILD_ENVIRONMENT=local

# Install necessary dependencies for building
# RUN apt-get update && apt-get install --no-install-recommends -y \
#     build-essential \
#     libpq-dev

# Copy requirements files and create wheels
COPY ./requirements /requirements
RUN pip wheel --wheel-dir /usr/src/app/wheels -r /requirements/${BUILD_ENVIRONMENT}.txt

# Set the run stage
FROM python as python-run-stage
ARG BUILD_ENVIRONMENT=local

ARG APP_HOME=/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

# Set working directory
WORKDIR ${APP_HOME}

# Copy wheels from build stage
COPY --from=python-build-stage /usr/src/app/wheels /wheels/

# Install necessary dependencies for running
# RUN apt-get update && apt-get install --no-install-recommends -y \
#    libpq-dev \
#    gettext \
#    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
#    && rm -rf /var/lib/apt/lists/*

# Install application dependencies
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* && rm -rf /wheels/

# Copy entrypoint and start scripts
COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# Copy the application code
COPY . ${APP_HOME}

# Set the entrypoint for the container
ENTRYPOINT [ "/entrypoint" ]
