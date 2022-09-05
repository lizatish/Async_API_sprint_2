FROM python:3.9

WORKDIR /opt

COPY tests/functional/requirements.txt $WORKDIR/tests/functional/requirements.txt

RUN pip install --upgrade pip && pip install --no-cache-dir -r $WORKDIR/tests/functional/requirements.txt

COPY tests/ /opt/tests
COPY fastapi-solution /opt/fastapi-solution

ENV PYTHONPATH "${PYTHONPATH}:/opt/tests/"
ENV PYTHONPATH "${PYTHONPATH}:/opt/fastapi-solution/src/"

