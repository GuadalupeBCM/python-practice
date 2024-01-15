FROM python:3.8

RUN apt-get update --yes && \
    apt-get upgrade --yes && \
    apt-get install --yes --no-install-recommends

RUN python3 -m pip install --no-cache-dir --upgrade jupyterlab

WORKDIR /root
COPY . /src/python-practice
RUN pip install -e /src/python-practice
