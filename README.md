# Flask API example

This project is a Flask API using Flask-SQLAlchemy, Flask-Caching, Flask-Migrations and Flask-RESTPLus extensions.

## Getting Started

To run this project you need to connect to a postgres (tested in 9.6)and redis server. You can simple run postgres and redis using docker.
With docker installed, to run postgres:

    docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=password -d postgres:9.6

And to run Redis:

    docker run -d -p 6379:6379 -i -t redis

## Pre requisites

This api was develoed using `python 3.7`. To install the requeriments run inside the `src` folder:

    pip install requirements.txt



## Authors

* **Marcos Camargo** - *Initial work* - [marcoscrcamargo](https://github.com/marcoscrcamargo)
