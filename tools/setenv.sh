#!/bin/sh

APIKEY="$1"
test -z $APIKEY && bash -c 'echo "API KEY was not specified as the first argument" ; exit 1'

export ANSIBLE_GALAXY_SERVER_RH_CERTIFIED_TOKEN="$APIKEY"
export ANSIBLE_GALAXY_SERVER_RH_VALIDATED_TOKEN="$APIKEY"