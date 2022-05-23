FROM python

RUN pip install Flask

RUN mkdir /app

COPY . /app

WORKDIR /app

ENTRYPOINT ["flask", "run"]