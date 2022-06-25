#!/usr/bin/bash

nmap -n -sP -PA -PU 192.168.1.0/24 | grep MAC > /home/dc/tools/red_bot/device_oth.txt 2>&1
cd /home/dc/tools/red_bot && ./scriptRed.py
