# Migrations

## Generate new one
This generates the migration file with the structure from the model in it.
This file will tell the migration script how to move up and down the upgrade
chain.

    docker-compose exec flask python ./manage.py db migrate

## Applying to the database
This is actually always applied once the containers are started.

    docker-compose exec flask python ./manage.py db upgrade

### Checking it out in postgress
It's often a good idea to check the final result in postgress.
This command drops you in a postgress shell in he docker container.

    docker-compose exec postgres psql -U flask
