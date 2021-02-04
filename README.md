# Docker Compose ECS Sample

This repository is the codebase used during the docker build talk on 02/04/2021. Entire talk is available at https://www.youtube.com/watch?v=2W_AQhWTmRw


# CheatSheet


## Run locally

```
docker compose up

```

## Create ECS Context

```
docker context create ecs --name FILL_ME_NAME
docker context use FILL_ME_NAME
```

## Create Secret in ECS Context to SecretManager

```
docker secret create pullcred /path/to/creds.json
```

## Deploy to AWS Cloud with

Find all the occurances of FILL_ME in `docker-compose.yaml` `docker-compose.prod.yaml` `docker-compose.prod-scaling.yaml` and `docker-compose.prod-rds.yaml`


* Run this to use MYSQL container

```
docker compose -f docker-compose.yaml -f docker-compose.prod.yaml -f docker-compose.prod-scaling.yaml up
```

* Run this to use RDS MQSQL

```
docker compose -f docker-compose.yaml -f docker-compose.prod.yaml -f docker-compose.prod-scaling.yaml -f docker-compose.prod-rds.yaml up
```

### Other tiny bits

* Use `--project-name` flag in compose commands to specify name of the CloudFormation stack, if you dont want the stack name to be the same as current folder's name


### Provide Feedback

* Regarding this repository - https://github.com/anshrma/docker-compose-ecs-sample/issues

* Regarding Docker Compose - https://github.com/docker/roadmap/issues

## Reach me

* Links to LinkedIn, Twitter, Email at https://github.com/anshrma