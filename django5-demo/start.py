import logging

from waitress import serve
from core.wsgi import application

logging.basicConfig(level=logging.DEBUG)

serve(application, 
      listen="0.0.0.0:8080",
      expose_tracebacks=True)
