# Bitstamp Utility Project
This is Bitstamp Utility project written Django (python).
It includes tools and bots for crypto trading at Bitstamp Exchange.

## Documentation

### Redis
Project includes Redis: Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache, and message broker.

## Development

### Local
In order to run this project you need to have docker-compose installed on your machine.
Run:
```
docker-compose up -d --build
```
Then:
```
docker-compose exec app bash
```
is going to provide you a shell with your environment (and build a docker image if it doesn't yet exist on your machine).
We suggest using docker for development.