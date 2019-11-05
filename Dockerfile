FROM python:3.7

ARG HOME=/usr/local

COPY ./src ${HOME}

WORKDIR ${HOME}

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["/usr/local/entrypoint.sh"]
