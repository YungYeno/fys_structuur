#! /usr/bin/python3.7

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/fys/wsgi')
#from app import main as application
from __init__ import create_app
application = create_app()