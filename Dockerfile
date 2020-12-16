FROM python

WORKDIR /home/root/docker-test

RUN touch "test.txt"

RUN mkdir /app
RUN cd /app

EXPOSE 8000

WORKDIR /

CMD ["/bin/bash", "-c", "'./app/start.sh'"]