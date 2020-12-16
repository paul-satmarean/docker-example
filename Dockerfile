FROM python

RUN mkdir /app
RUN cd /app

WORKDIR /

CMD ["/bin/bash", "-c", "'./app/start.sh'"]