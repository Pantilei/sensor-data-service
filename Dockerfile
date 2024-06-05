FROM python:3.12

ENV PYTHONUNBUFFERED 1

# EXPOSE 8000
WORKDIR /app


RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat-traditional && \
    apt-get install -y --no-install-recommends git &&\
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY healthcheck.py /usr/bin/healthcheck
RUN chmod +x /usr/bin/healthcheck
HEALTHCHECK --interval=30s --timeout=1s --retries=3 CMD healthcheck || exit 1

COPY poetry.lock pyproject.toml ./
RUN pip install poetry && \
    poetry config virtualenvs.in-project false && \
    poetry install --only main

COPY . ./
