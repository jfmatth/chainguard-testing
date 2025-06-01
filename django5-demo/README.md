# Django demo for Chainguard and UV

## requirements
- Uses waitress for serving django versus gunicorn

Waitress is installed as an .EXE on Windows in the .venv/scripts/ folder, so need to add that to Dockerfile path

## running local (Windows powershell)
```
uv sync
.venv\scripts\activate.ps1
 waitress-serve.exe --host=0.0.0.0 --port=8080 core.wsgi:application
 ```

