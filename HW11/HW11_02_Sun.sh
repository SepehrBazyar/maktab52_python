#!/bin/bash
#Written by: Sepehr Bazyar
read -p "Please Enter the Latitude  in Decimal Degrees(Tehran = 35.6961): " lat
read -p "Please Enter the Longitude in Decimal Degrees(Tehran = 51.4231): " lng
curl "https://api.sunrise-sunset.org/json?lat=$lat&lng=$lng"
