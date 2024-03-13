FROM kong:3.6.1

USER root

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-dev libffi-dev gcc g++ file make && \
    PYTHONWARNINGS=ignore pip3 install kong-pdk geopy

WORKDIR /opt

USER kong

EXPOSE 8000 8443 8001 8444

STOPSIGNAL SIGQUIT

HEALTHCHECK --interval=10s --timeout=10s --retries=10 CMD kong health

