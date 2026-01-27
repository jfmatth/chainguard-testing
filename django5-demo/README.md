# Django demo for Chainguard and UV

## Requirements
- Podman using WSL
- Uses waitress for serving django versus gunicorn
- UV by Astral

## Running local (Windows powershell)
```
uv sync
.venv\scripts\activate.ps1
start.py
```

## start.py
use this since Windows and Linux have different waitress-serve commands and I wanted to be consistent.

## Building the Dockerfile
Uses a two-stage build, saves 700mb of image size

On Windows with Podman
```
podman machine start
podman build . -t django5-demo
podman run -p 8080:8080 django5-demo
```

## Dockerfile info

The important part for more Django stuff is the COPY lines, make sure you copy over all Django apps, for example:
```
    COPY manage.py /app
    COPY start.py /app
    COPY core/ /app/core
```

```core``` is the main Django folder with settings, urls, wsgi, etc.  Other app folders must be copied as well