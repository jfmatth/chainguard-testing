# Django demo for Chainguard and UV

## requirements
- Uses waitress for serving django versus gunicorn

## running local (Windows powershell)
```
uv sync
.venv\scripts\activate.ps1
start.py
 ```

## start.py
use this since Windows and Linux have different waitress-serve commands and I wanted to be consistent.

## Dockerfile
Uses a two-stage build.  

The important part for more Django stuff is the COPY lines, make sure you copy over all Django apps, for example:
```
    # copy application files to WORKDIR (/app)
    COPY manage.py /app
    COPY start.py /app
    COPY core/ /app/core
```

```core``` is the main Django folder with settings, urls, wsgi, etc.  Other app folders must be copied as well