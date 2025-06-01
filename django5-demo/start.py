from waitress import serve

from core.wsgi import application

serve(application, 
      listen="0.0.0.0:8080",
      expose_tracebacks=True)
