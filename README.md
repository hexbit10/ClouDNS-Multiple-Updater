# ClouDNS Multiple Domain Updater
This is the source to a docker image that uses the environment variable "DOMAIN_LIST" and reads it as a json object. 
DOMAIN_LIST should be a stringified version of a json list.
Example:

DOMAIN_LIST='["https://ipv4.cloudns.net/api/dynamicURL/?q=<token1>", "https://ipv4.cloudns.net/api/dynamicURL/?q=<token2>"]'
