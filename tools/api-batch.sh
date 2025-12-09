#!/bin/sh

METHOD="$1"
URL="$2"
ADMIN_USERNAME="$3"
ADMIN_PASSWORD="$4"
BATCH_SIZE="${BATCH_SIZE:-30}"

echo "Starting infinite load test"

while true; do

  echo "--- Firing batch of $BATCH_SIZE request ---"

  for ((i=1; i<=BATCH_SIZE; i++)); do
      curl -skL -o /dev/null -u "${ADMIN_USERNAME}:${ADMIN_PASSWORD}" -X "${METHOD:-GET}" "$URL" &
  done

  # waits for all background processes to be done
  wait

  echo "--- Batch finished ---"
done