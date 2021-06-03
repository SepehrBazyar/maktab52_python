#!/bin/bash
#Written by: Sepehr Bazyar
read -p "Please Enter the Latitude  in Decimal Degrees(Tehran = 35.6961): " lat
read -p "Please Enter the Longitude in Decimal Degrees(Tehran = 51.4231): " lng
curl "https://api.sunrise-sunset.org/json?lat=$lat&lng=$lng" > "Sun.json"

if [ $(cat "Sun.json" | python -m json.tool | grep '\"status\"' | cut -d ':' -f 2) == '"OK"' ];
then
    echo "Tolou Aftab: $(cat "Sun.json" | python -m json.tool | grep '\"sunrise\"' | cut -d ':' -f 2-4 | cut -c3-12)"
    echo "Qorub Aftab: $(cat "Sun.json" | python -m json.tool | grep '\"sunset\"' | cut -d ':' -f 2-4 | cut -c3-12)"
else
    echo "INVALID_REQUEST: Indicates that Either lat or lng Parameters are Missing or Invalid!"
fi
