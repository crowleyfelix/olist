# Olist

This project is an API that provide endpoints to record and calculate telephone calls based on these [specs](docs/SPECIFICATION.md).

## Installing

### Prerequisites

- [docker] 18.03.1-ce
- [docker-compose] 1.21.2

Execute the following command to start the application:

`docker-compose up -d`

To stop, execute:

`docker-compose down`

## Requesting

To interact with the API, please, check the api [docs](docs/swagger.yml) built with swagger for verify the available resources and expected requests.

You could read the raw file, or use a [swagger viewer] to visualize de documentation.

There is an already working environment on url https://olist-call-recorder.herokuapp.com/api for test proposals.

## Contributing

Please, read the [Contributing](docs/CONTRIBUTING.md) file for development instructions.

[docker]:https://www.docker.com/community-edition#/download
[docker-compose]:https://docs.docker.com/compose/install/
[swagger viewer]: https://marketplace.visualstudio.com/items?itemName=Arjun.swagger-viewer