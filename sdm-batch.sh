#!/bin/bash

python3 ./sdm.py -m SDM630 -a 1 -o influxlineprotocol
python3 ./sdm.py -m SDM630 -a 2 -o influxlineprotocol
python3 ./sdm.py -m SDM630 -a 3 -o influxlineprotocol
python3 ./sdm.py -m SDM230 -b 9600 -a 4 -o influxlineprotocol
python3 ./sdm.py -m SDM230 -b 9600 -a 5 -o influxlineprotocol
python3 ./sdm.py -m SDM220 -b 9600 -a 6 -o influxlineprotocol
