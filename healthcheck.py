#!/usr/local/bin/python3
import sys

import requests

try:
    requests.get("http://localhost:8000/healthy")
except:
    sys.exit(1)
