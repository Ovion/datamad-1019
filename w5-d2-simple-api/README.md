## Compile docker image
    docker build -t simple-api .


## Run the creaated image
    docker run simple-api


## Deploy en heroku
**WARNING** Debe de ser un repositorio nuevo de git solo con el codigo del proyecto

    heroku login
    heroku create miapi1019
    heroku container:push api --app miapi1019
    heroku container:release api --app miapi1019