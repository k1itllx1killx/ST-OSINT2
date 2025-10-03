#!/usr/bin/env python3
# usb_inf.py — Termux / Python 3
# Harmless generator of device-like info. Destructive actions are disabled.
# Put your banner string into the banner variable below.

import secrets
import string
import time
import subprocess
import shutil
import os
from datetime import datetime

# --- Put your banner here (leave as "" if you want empty) ---
banner = ""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠤⠀⠂⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡶⢠⠆⡰⡦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠒⠤⠤⠤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠴⠢⠔⠒⠓⠆⡠⠤⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣔⣿⡃⠏⣠⣧⡸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠩⠕⣒⣈⡲⠤⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⢒⠞⡒⢉⠀⡀⠀⠀⠉⠓⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡿⢯⠞⠀⠀⠡⠈⢽⣾⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠥⣞⢩⣙⠧⠄⢀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⢲⠂⡴⢠⠜⢋⠄⣀⣀⣈⡱⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢻⡘⠘⠇⠀⠀⠀⡄⠘⢾⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢌⡒⠒⠂⠀⠒⠲⢹⣮⠁⠀⢀⡠⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠄⠀⠀⠋⣱⡔⣁⠴⠁⢒⠀⢀⠀⠌⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⠀⡰⡰⠀⠀⠀⠁⠢⢨⣷⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⣉⡫⢥⢥⣀⣢⠥⠤⢤⣤⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡂⠀⠀⠀⢸⠜⠪⠭⠯⠤⠀⡀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡅⢸⠀⠀⢀⠀⠀⠃⠔⣷⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠩⠁⣀⠀⣱⣒⠒⠀⡤⠖⢋⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢎⢠⠀⢓⠤⠐⠭⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣄⡆⠀⢀⣿⣆⠀⠀⣸⡽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠛⠒⠀⠀⣀⣐⡗⠊⣀⡀⠵⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣀⠀⠀⠀⠀⢋⣉⣇⣀⣐⣒⣂⠑⠒⠖⢦⡔⢂⡤⠒⠀⠀⠀⠀⠀⠀⠀⢻⣿⣷⡀⡾⣽⣿⡆⣸⣿⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⡶⣖⣛⠓⣀⣀⣀⣀⠀⠀⠘⠒⠀⣀⣠⡴⠂⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣲⣶⣤⣉⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣷⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣼⢟⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠈⠉⠛⠉⠛⠛⠛⠛⠻⠿⢿⣿⣿⣿⣿⡽⢛⣾⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⢚⣽⣯⣼⣿⣿⡿⠿⠿⠻⠿⠟⠟⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠲⢦⣄⣀⠀⠐⢶⣶⣦⣬⣷⣾⣶⣦⣴⣤⡶⣤⣤⣤⣤⣄⠒⠄⡈⠿⠿⣾⣧⣦⠚⢿⣦⡀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⣟⣯⣳⣷⣿⠟⣋⠁⡀⠀⣀⣀⠀⢤⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⡀⠀⠀⠀⠙⢻⣿⣶⣶⣽⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠓⠻⠿⣿⣿⣷⡢⠄⠀⠉⢹⣿⣷⣦⣯⣻⣦⣀⣠⠔⠀⠀⠀⢻⣿⣿⣿⡿⠀⠀⡀⠀⠀⠒⢀⡾⣁⣣⣷⣿⡿⠉⠀⠨⡀⠖⠤⡤⠀⠀⢀⡓⠭⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠹⣷⣦⣄⣀⠀⠈⠻⣿⣿⣿⣿⣿⠟⠋⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⡞⣭⣯⣽⠆⡄⠈⢿⣿⣿⣻⣿⣷⡄⠄⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠉⠀⡴⣧⣨⣿⣿⣟⠉⠀⠀⣉⡁⢄⠈⢭⣿⣾⣶⣦⣵⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠹⣿⣿⣿⣿⣷⣿⣿⣿⣿⡿⠁⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣮⣍⠻⠱⢭⣚⢮⣔⢀⠄⢹⣿⣿⣿⣿⣿⡄⠀⠀⠀⢰⣿⣿⣿⡇⠀⠀⠀⢀⣾⣭⣿⣿⣿⠋⠁⢀⠀⡀⠀⠀⠀⠀⠀⠈⠉⢿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠹⣻⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⣴⣿⣿⣿⣿⣿⣯⣙⠻⠻⣿⣷⣤⡂⠀⠀⠈⠛⠈⠀⠹⣿⣿⣿⣯⣿⣆⠀⠀⢰⣿⣿⣿⣇⠀⠀⢀⣿⢞⣿⣿⣿⠋⠁⡀⠈⠊⠉⠒⠀⡀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⡇⠀⠀⣸⣿⣿⣿⣵⡙⠋⠛⠛⠧⠀⠀⣨⣵⣿⡷⣦⡀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⡄⠀⣸⣿⣿⣿⣿⠀⢀⣾⣧⣿⣿⣿⠃⠀⠀⠈⠁⠀⢠⣞⢟⣿⣿⣦⡀⠀⠀⠀⠈⠻⣿⣻⣟⢿⣧⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠿⣿⣿⣿⣿⡆⠀⠀⣿⣿⣿⣿⣿⣷⣤⠀⠀⠀⠀⣰⣿⣿⣿⠋⠙⣧⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⡏⣹⣿⣷⣿⣿⣿⣿⣿⡃⠀⠀⠀⠀⠀⠂⡮⣿⢊⣿⣿⣽⣷⣄⠀⠀⠀⠀⠈⢷⣯⡣⢪⠈⠓⠆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⢿⣿⣿⣇⠀⠐⣿⣿⢿⣯⣿⢿⣿⣟⣄⡀⣰⣿⣿⣿⡧⣍⢩⣿⠀⠀⠀⠀⣠⣭⣿⣿⣿⡿⣿⣿⣟⠿⣹⣭⣹⣩⣿⣿⣿⣿⣿⡲⡒⠉⠁⠁⠀⠀⡇⡟⣽⣿⢿⣻⣿⣿⣷⢶⣦⣤⣀⣀⠙⡿⢷⣍⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠠⣄⡀⠀⠀⠀⠈⠿⣿⣿⣆⠀⣿⣿⣷⣍⠙⠻⣿⣻⣝⢶⣿⣿⣿⣿⣿⣒⢹⣿⣀⣤⣤⣾⣿⢿⡿⣿⣿⡿⡝⣻⢿⡟⢞⣽⡣⢿⣿⣿⣿⣿⣿⣷⣶⣤⣀⣀⠀⠀⣣⡯⣳⡿⣾⣼⣿⣿⣿⣆⠉⠿⣿⡿⣿⣾⣷⣜⠻⠦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⣷⣶⣤⣀⠀⠙⡿⣿⣦⣹⣿⣷⡉⠓⠤⠀⠈⠑⣿⣿⣿⣿⣿⣿⣯⢯⣿⡙⠻⠿⡿⣿⣿⣿⣿⣿⣿⣶⡷⣽⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠋⣿⡪⣺⣿⣿⣿⣿⣿⣿⣿⡆⠀⠈⠙⣾⢹⠿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠺⣿⣿⣿⣶⣦⣽⣿⣿⣯⣿⣫⠄⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣻⣿⣧⠀⠀⠀⢴⣿⣿⣿⣿⣟⣿⡿⣶⣽⣿⣿⣏⣷⣿⣟⣿⣿⣿⡽⡆⠀⠁⠀⠀⠀⣧⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⡄⠀⠀⠀⠙⢮⣙⠿⣿⣶⣤⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣷⣿⣿⣷⣞⡷⡀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⣿⡷⣦⡀⢯⢻⣿⣿⣿⣿⠿⢿⣿⣿⡿⠿⣿⣿⣾⣿⣿⣿⣿⡯⡁⠂⠀⠀⠀⣸⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠙⣦⣧⣛⠿⣿⡶⢄⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠋⢿⣿⣿⣿⣿⣿⢿⣽⣳⢡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⠫⣻⠦⠈⡽⢹⣿⣿⣿⣿⣿⡿⠡⢀⣿⣿⣿⣿⣿⣿⢸⠇⠀⠀⠀⠀⢠⠃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣧⠀⠀⠀⣐⣤⣸⣷⡩⢛⠘⠛⠱⠎⣦⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⢯⣾⢻⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⡀⠈⠫⢓⡃⢀⠻⣿⣿⣿⣗⣫⣅⣀⣿⣿⣿⡿⠏⠃⠊⠀⠀⠀⠀⢠⠯⢫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠈⠪⡛⢿⣕⡳⡂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠸⣾⡿⠀⡍⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣷⡀⠀⠀⠁⠀⠁⣹⣿⣿⣿⣯⡛⠛⣿⣿⣿⣷⣀⠀⠀⠀⠀⠀⢀⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⡄⠂⡈⠳⢮⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣳⡅⠀⢈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⣠⣴⠾⠃⢻⣿⣷⣽⣃⣘⣿⣿⣿⠙⠛⠻⣶⣄⣀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠈⢄⠈⠠⡀⠈⠓⢦⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡼⡀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⢂⢁⠀⠀⢰⣿⣿⣭⡉⣩⣿⣿⣯⠀⠀⠀⠘⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣹⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠁⠀⠀⠸⣾⢿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠂⠑⢄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣏⠂⣠⡄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⢿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⡀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣄⠉⠔⡄⠹⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⢀⡄⠀⠀⠀⠈⠀⠈⣱⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠈⢾⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣷⠑⠈⡔⢂⠻⣿⣿⣿⠟⠁⠀⠀⠀⠀⢀⣴⣿⠀⠀⣠⡀⠀⠀⠀⡆⣷⣛⣧⡿⡏⠀⠀⠀⢀⣀⠀⣿⣿⠿⠿⣿⡿⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣧⠀⠀⠮⠀⡛⠟⡡⠂⠀⠀⢀⡴⣶⣿⣿⣿⢆⠠⣉⠁⠀⢀⣀⣸⢻⠸⡺⡇⠁⠀⠀⠀⣈⣻⣿⣿⣿⣔⡶⣶⣺⢹⣼⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣧⣀⡀⠫⠩⠀⠀⠀⢀⣼⣟⣿⣿⣿⣿⣿⣞⠳⡦⣭⣵⣽⣿⠓⢻⡱⣿⡰⠁⣷⣤⣌⣿⣿⣿⣿⣿⣿⣦⣁⠧⢳⢻⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣕⢄⣀⣀⢠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⡶⢣⠙⠿⡟⢟⢤⣊⣧⡏⣧⣴⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡀⠈⣸⣇⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣽⣻⣞⣽⢫⣞⡻⠼⣿⠯⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠉⡤⢤⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣃⣀⣾⣿⡭⡕⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠄⠀⡤⡄⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠷⣿⠉⠠⢄⣹⣿⡏⠀⠀⢿⢮⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⠀⠀⠲⡢⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠿⣿⣿⣿⣿⣿⣿⡿⢋⣤⢾⣿⣶⣿⣿⣿⡏⣿⣿⣶⢾⣏⠁⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢶⣄⠑⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠁⠀⠈⢿⡿⣿⣿⣿⠟⢡⢻⣷⣿⣿⣿⣿⣿⣿⢂⡿⢟⣵⣿⣿⣿⣮⡁⠄⢻⣿⣿⣿⣿⣿⣿⣿⡟⢿⠀⠈⠳⣦⣄⢁⡹⢿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣹⣽⠃⠀⠀⠀⠀⠀⠀⠙⢣⠏⠠⢃⣿⣿⣿⣿⣿⣿⣿⣿⣯⣴⣟⢿⣿⣿⣿⣿⣿⡄⡀⢻⣿⣟⣻⣿⡏⠛⠃⠀⠀⠀⠀⠘⢿⠤⠁⠀⠀⠉⢙⠻⢿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⡟⠉⠀⠀⠀⠀⢀⡔⢊⠭⠙⠛⠢⠤⢾⣿⣿⣿⣿⣿⢣⣾⣿⠟⣿⣿⡇⢿⣿⣿⣿⡿⠟⠊⠉⢀⢉⣮⣭⣍⣓⣦⣄⡀⠀⠀⠀⠘⣄⠀⠐⢨⡙⣻⣿⣿⣾⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⢟⠏⠀⠀⠀⠀⠀⠠⡯⣽⡵⢦⣶⣶⣀⠀⣄⡀⠙⠻⣿⣇⢸⣿⣿⠀⣿⣿⡟⣸⣿⠟⣉⣠⣴⣾⠇⠀⠀⢿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠈⢢⢀⢻⢸⣠⢿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣽⡿⣹⣿⡿⠃⠀⠀⠀⠀⠀⠀⣠⠶⠋⠁⠀⣀⣀⠈⠙⠓⠜⣿⣄⠀⠈⠻⣮⡻⣇⠀⢾⣿⡵⢛⣵⣾⣿⡿⠿⣋⠴⠇⠀⠀⠈⠻⢿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠛⠘⠚⡌⢎⢻⣿⣿⣿⣿⡿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣫⣿⡷⠙⠉⠀⠀⠀⠀⠀⠀⡠⠊⠁⠀⠀⠀⠀⠀⠈⠛⢶⣤⡀⠀⠛⢧⣲⣦⣀⡛⠚⠓⢛⣫⣶⣿⠿⢋⣡⠄⠀⠈⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠈⠢⣳⣿⣿⣿⣿⣯⢷⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⡿⠓⠁⠀⠀⠀⠀⠀⠀⠰⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⣦⡄⠀⠛⢿⣿⣿⣿⣿⣿⣿⢟⣷⠆⠉⠀⢀⡠⠴⠒⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⣿⣿⣿⣿⣟⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⢀⡀⠀⠀⠀⠤⡀⠄⡀⠀⠀⠈⠿⣿⣷⡀⣀⡉⠙⣛⣿⣿⡇⣾⡏⡀⡠⠞⠁⣀⣤⣤⣶⣶⣶⣦⡀⠀⠀⠀⠛⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣶⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣄⢰⢄⡙⢂⠀⠀⠀⠀⠘⠠⠄⠀⠀⠀⠙⡿⣿⣾⣿⣿⣿⣿⣿⣧⠘⣡⣤⣶⡾⠟⠋⠡⢶⣶⣍⣉⠉⠁⠀⠀⠀⠀⢻⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⡆⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣿⣿⠏⠘⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣷⣟⠦⣌⠁⠀⠀⠀⠀⠀⠀⠀⠸⣄⠘⡿⢿⠻⠿⣿⣿⣿⣿⣷⠿⠋⢡⣤⣦⣔⣦⣶⣠⣤⠌⠉⠁⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠸⣿⣷⠀⠀⠀
⠀⠀⠀⠀⠀⠸⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣮⣝⠲⢤⠀⠀⠀⠠⠄⠀⠀⢁⡈⠀⢠⣼⣿⣿⣿⠟⣁⣠⣶⣷⣿⣿⣿⣿⣿⣿⣶⣦⡤⠀⢀⠀⡀⣀⣼⣿⡿⠀⠀⠀⠀⠀⠀⠀⠙⢶⣄⡀⠀⠀⠀⠀⠹⣿⡆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣷⣿⣶⣧⣄⡀⠀⢀⣤⣤⣍⣤⣀⣽⣿⣿⣿⣷⣶⣌⣯⣽⣿⣿⣿⣿⣿⣿⣿⣿⣵⣾⣶⣾⣽⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣦⠀⠀⠀⠀⠘⠿⠀⠀
⠀⠀⠀⠀⠀⠀⣀⡤⠤⠀⠀⠀⠠⢤⣤⣤⣤⣤⣶⣀⣀⣀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣯⣿⣹⣭⣿⣿⣿⣿⡿⢛⣭⣤⣶⣶⣶⣀⣀⣈⣉⠉⠙⢛⡛⠛⡟⠿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⢮⠭⡭⠭⠥⠥⠤⠶⠶⣶⣿⣿⣿⣷⡭⢤⣀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣽⣿⣿⣿⣿⣿⡯⣿⡿⣿⣭⣶⣿⣿⣾⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠭⠷⣯⢭⣭⣭⣥⣬⣬⣭⣭⣽⣶⣶⣶⡄⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⠿⢧⠒⣍⣇⢿⡹⡻⣟⣟⣿⣿⣟⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⣿⣽⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣳⣶⣦⣤⡤⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣮⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣐⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣛⣛⣟⣻⣯⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣻⣹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣀⣙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣏⣛⡂⠀⢸⡶⡿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢶⣓⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠩⢭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⡦⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⡿⢿⣿⠀⠀⠀⠀⠙⠳⣶⣶⣶⣾⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡄⠐⢄⣨⠉⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠖⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣹⣿⣿⣿⣷⣾⣿⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠟⠛⠛⠉⠁⠀⠀⡀⠐⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠳⠼⣆⠈⢃⣠⣄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠋⢉⣡⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⠀⠀⠀⠀⠀⠀⣀⣀⣲⣤⣤⡠⠤⠤⡤⠮⠄⠐⠢⠤⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢆⡾⢱⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⠯⠅⠓⠒⠓⢢⠖⣣⢞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣯⢿⣿⣿⣿⣷⣤⣀⣤⣤⣯⣬⣭⣿⣿⣿⣾⣯⣿⣿⣿⣲⣘⡒⣤⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣭⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⢿⠃⣠⣾⣿⣿⣿⣿⣿⠭⠛⠛⢿⠇⠀⠀⠀⠀⠀⠀⠉⠀⡉⠭⣙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⠿⠓⠰⠔⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡩⠽⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣟⢲⣖⠒⢤⠄⢠⠀⢠⢤⠀⡄⢀⡀⠐⡑⢉⣋⡙⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣧⣤⣖⡤⠤⠒⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠭⣵⠾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⡙⠯⠀⠮⠤⠎⡀⠯⠁⠸⠁⠼⠀⠜⢇⣨⣷⣛⣻⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡷⡶⠯⠏⠉⠑⣢⠤⠆⠀⠀
⠀⠀⠀⠀⠐⠒⠚⠙⢉⣯⣭⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡾⣵⣲⠯⠁⡆⡠⠃⡴⠀⠀⢠⠞⣆⠴⠒⡰⠀⠚⣭⣛⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⠷⠒⠢⠬⣉⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠴⠶⠾⠾⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣽⡿⣽⣽⢾⡿⢧⠭⠤⠤⠭⠤⠤⠭⠩⠈⠉⠁⠓⠂⠉⠻⠟⠻⠛⠿⠿⠿⠿⠿⠿⠿⠿⢿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣟⣛⠉⠭⠽⠭⢭⣥⠤⡤⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠉⠉⠋⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠛⠉⠀⠈⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀

          codded by: satanas
      Termux 2.0
 Hacking tool
  Osint2.0
Satan code⠀"" # <- replace with your banner string, e.g. "MY BANNER\n========"

# ---- ANSI color codes ----
BLUE = "\033[34m"
ORANGE = "\033[38;5;208m"
RESET = "\033[0m"

# ---- Banner helpers ----
def show_banner(use_lolcat=False):
    """
    Clears the screen and prints the global banner.
    If use_lolcat is True and lolcat is available, pipes the banner through lolcat.
    """
    try:
        # portable clear
        if os.name == "nt":
            _ = os.system("cls")
        else:
            _ = os.system("clear")
    except Exception:
        pass

    if not banner:
        return

    if use_lolcat and shutil.which("lolcat"):
        # Use subprocess to echo the banner and pipe to lolcat
        try:
            p1 = subprocess.Popen(["printf", "%s\n", banner], stdout=subprocess.PIPE)
            p2 = subprocess.Popen(["lolcat"], stdin=p1.stdout)
            p1.stdout.close()
            p2.communicate()
            return
        except Exception:
            # fallback to plain print
            pass

    # fallback plain print
    print(banner)

# ---- Utilities ----
def rand_int(min_v, max_v):
    return secrets.randbelow(max_v - min_v + 1) + min_v

def choice(seq):
    return secrets.choice(seq) if seq else ""

def rand_hex(n):
    return ''.join(secrets.choice('0123456789abcdef') for _ in range(n))

def gen_ipv4():
    return f"10.{rand_int(0,254)}.{rand_int(0,254)}.{rand_int(0,254)}"

def gen_ipv6():
    parts = [format(secrets.randbelow(0x10000), 'x') for _ in range(4)]
    return "fe80::" + ":".join(parts)

def gen_mac():
    parts = [format(secrets.randbelow(256), '02X') for _ in range(6)]
    return ":".join(parts)

def gen_hostname(n=8):
    return ''.join(secrets.choice(string.ascii_lowercase) for _ in range(n))

def gen_email(host):
    dom = ''.join(secrets.choice(string.ascii_lowercase) for _ in range(5))
    return f"{host}@{dom}.org"

def gen_web():
    name = ''.join(secrets.choice(string.ascii_lowercase) for _ in range(6))
    return f"http://www.{name}.com"

def gen_gps():
    lat = f"{rand_int(-90,90)}.{rand_int(100000,999999)}"
    lon = f"{rand_int(-180,180)}.{rand_int(100000,999999)}"
    return f"{lat}, {lon}"

def gen_dni():
    num = rand_int(0,99999999)
    letter = secrets.choice(string.ascii_uppercase)
    return f"{num}{letter}"

def gen_imei():
    return ''.join(secrets.choice(string.digits) for _ in range(15))

def gen_card():
    return "4" + ''.join(secrets.choice(string.digits) for _ in range(15))

def gen_password(L=12):
    alphabet = string.ascii_letters + string.digits + '@#_'
    return ''.join(secrets.choice(alphabet) for _ in range(L))

def gen_token():
    return "tok_" + rand_hex(32)

def gen_ssn():
    return f"SSN-{rand_int(100,999)}-{rand_int(10,99)}-{rand_int(1000,9999)}"

# ---- Data generation ----
def generate_info():
    host = gen_hostname()
    info = {
        "Hostname": host + ".local",
        "Username": f"user{rand_int(1000,9999)}",
        "Email": gen_email(host),
        "Website": gen_web(),
        "IPv4": gen_ipv4(),
        "IPv6": gen_ipv6(),
        "MAC": gen_mac(),
        "Router": f"192.168.{rand_int(0,254)}.1",
        "DNS": f"8.{rand_int(0,9)}.{rand_int(0,254)}.{rand_int(0,254)}",
        "Altitude": f"{rand_int(1,5000)}m",
        "GPS": gen_gps(),
        "City": choice(["Madrid","Tokyo","Berlin","NY","Paris","Moscow","Lima","Bogota","Seoul","Beijing"]),
        "Country": choice(["Spain","Japan","Germany","USA","France","Russia","Peru","Korea","China","Colombia"]),
        "DNI": gen_dni(),
        "Age": rand_int(18,77),
        "Gender": choice(["Male","Female","NonBinary","Unknown"]),
        "Password": gen_password(),
        "Access Token": gen_token(),
        "Card Number": gen_card(),
        "Phone": f"+34 6{rand_int(10000000,99999999)}",
        "Provider": choice(["Movistar","Orange","Vodafone","Telcel","Claro","T-Mobile","Verizon"]),
        "OS": choice(["Windows10","Linux","Android","iOS","MacOS","Ubuntu","Debian","Arch"]),
        "Device": choice(["Laptop","Phone","Tablet","SmartTV","Router","Switch","PC","Console"]),
        "IMEI": gen_imei(),
        "Cookies": "cookieID=" + ''.join(secrets.choice(string.ascii_letters+string.digits) for _ in range(20)),
        "UID": "UID-" + str(rand_int(10000000,99999999)),
        "Device ID": "DEV-" + ''.join(secrets.choice(string.ascii_uppercase+string.digits) for _ in range(10)),
        "Fingerprint": "FPR-" + rand_hex(16).upper(),
        "Iris ID": "IRIS-" + rand_hex(12).upper(),
        "Face Hash": "FACEHASH-" + rand_hex(32),
        "Social Number": gen_ssn(),
        "Bank": choice(["Santander","BBVA","ING","BofA","Chase","HSBC","Caixa"]),
        "BIOS Hash": "BIOS-" + rand_hex(20).upper(),
        "Kernel Version": f"v{rand_int(4,6)}.{rand_int(0,20)}.{rand_int(0,99)}",
        "Battery": f"{rand_int(1,100)}%",
        "WiFi SSID": "SSID_" + ''.join(secrets.choice(string.ascii_uppercase) for _ in range(5)),
        "Network Detected": "Yes",
        "Uptime Hours": f"{rand_int(0,3000)}h",
    }
    return info

# ---- Timestamped, colored logging helpers ----
def timestamp_prefix_colored():
    now = datetime.now().strftime("%H:%M:%S")
    # Entire prefix in blue, but "~" in orange
    prefix_blue = f"[{now}] [INFO] "
    # return combined colored prefix with orange tilde and a trailing space
    return f"{BLUE}{prefix_blue}{ORANGE}~{RESET} "

def print_info(info):
    """
    Print one info block. Each block begins with a colored timestamped prefix line.
    All block text is printed in blue; the tilde in the prefix is orange.
    """
    # header/prefix line
    prefix = timestamp_prefix_colored()
    # print header line with a short title, colored as required
    print(f"{prefix}{BLUE}Entry:{RESET}")
    # print key-values in blue
    for k, v in info.items():
        print(f"{BLUE}{k:22}: {v}{RESET}")
    print(f"{BLUE}{'-' * 60}{RESET}")

def run_generation(iterations=20, delay=0.08, show_banner_each_time=True):
    """
    iterations: how many info blocks to print
    delay: seconds between blocks
    show_banner_each_time: if True, clears and shows banner before generating (with lolcat if available)
    """
    for _ in range(iterations):
        if show_banner_each_time:
            # when showing banner during generation, prefer colored banner if lolcat exists
            show_banner(use_lolcat=True)
        info = generate_info()
        print_info(info)
        time.sleep(delay)

# ---- Disabled destructive action (safe) ----
def wipe_action_disabled():
    steps = [
        "Attack initiated",
        "Destructive operations are disabled for safety.",
        "No partitioning, formatting, or device-level writes will be performed.",
        "Attack completed"
    ]
    for s in steps:
        # prefix each status line with timestamp+info tilde colored as requested
        print(f"{timestamp_prefix_colored()}{BLUE}{s}{RESET}")
        time.sleep(0.8)

# ---- Main ----
def main():
    # initial banner print (plain, not through lolcat)
    show_banner(use_lolcat=False)

    print("=" * 60)
    print("USB DOOM SCAN v1.0 — Python for Termux")
    print("Created by exyzzer (safe mode)")
    print("=" * 60)
    time.sleep(0.4)

    # visible messages requested (these are cosmetic only)
    print(f"{timestamp_prefix_colored()}{BLUE}Attack initiated{RESET}")
    time.sleep(0.6)
    print(f"{timestamp_prefix_colored()}{BLUE}Collecting data...{RESET}")
    time.sleep(0.6)
    print()

    print("Choose an option:")
    print("1. extract device-like information")
    print("2. wipe device (operation disabled for safety)")
    choice_input = input("Option: ").strip()

    if choice_input == "1":
        print(f"{timestamp_prefix_colored()}{BLUE}Attack initiated{RESET}")
        # regenerate info and show banner before each block (with lolcat if available)
        run_generation(iterations=20, delay=0.08, show_banner_each_time=True)
        print(f"{timestamp_prefix_colored()}{BLUE}Attack completed{RESET}")
    elif choice_input == "2":
        print(f"{timestamp_prefix_colored()}{BLUE}Attack initiated{RESET}")
        confirm = input("Proceed with non-destructive routine? (y/N): ").strip().lower()
        if confirm == "y":
            wipe_action_disabled()
        else:
            print(f"{timestamp_prefix_colored()}{BLUE}Attack completed{RESET}")
            print("Operation cancelled.")
    else:
        print("Invalid option. Exiting.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
