- Build the initial project
```
uv init .
```

- Add various packages via ```uv add```
    - This will add to the pyproject.toml

- ```Dockerfile``` accounts for .venv getting built when you sync
- Build
```podman build . -t test1```
