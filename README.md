# ClouDNS Multiple Domain Updater
## Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [Links](#links)

## General info
This is the source to a docker image that updates Dynamic DNSs, specifically those set up with the provider ClouDNS. It works by using a python script and a cron job. 
Example:

## Setup
The container uses a mounted .env file with the environment variable "DOMAIN_LIST" that has to be mounted to the inside location "/app/.env" and reads it as a json object. DOMAIN_LIST should be a stringified version of a json list.

### .env:
```
DOMAIN_LIST='["https://ipv4.cloudns.net/api/dynamicURL/?q=<token1>", "https://ipv4.cloudns.net/api/dynamicURL/?q=<token2>"]'
```

### Example for a docker-compose.yml:
```
version: "3.9"
services:
  app:
    image: "hexax/cloudns-multiple-updater:v12"
    volumes:
      - ./.env:/app/.env
```

## Links
* [Github: ClouDNS-Multiple-Updater](https://github.com/hexax2/ClouDNS-Multiple-Updater)
* [Docker Image Page: cloudns-multiple-updater](https://hub.docker.com/r/hexax/cloudns-multiple-updater)
