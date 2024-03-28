#!/bin/bash

TARGET_IP="192.168.2.5 -Pn"
TIMESTAMP=$(date +"%Y%m%d%H%M%S")

echo "Timestamp: $TIMESTAMP"


OUTPUT_FILE="output_${TIMESTAMP}.xml"

nmap -sV -p 80 --script=http-enum -oX $OUTPUT_FILE  $TARGET_IP

HTML_OUTPUT_FILE="output_${TIMESTAMP}.html"

xsltproc $OUTPUT_FILE -o $HTML_OUTPUT_FILE

