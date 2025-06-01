# Chainguard python-dev has UV installed
FROM cgr.dev/chainguard/python:latest-dev as builder

ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/.venv/bin:$PATH"

USER root

# use /app generic folder
WORKDIR /app

# use python venv to bring in any necessary packages
# RUN python -m venv /app/venv
COPY pyproject.toml  .
RUN uv sync 


# Chainguard Python does not have UV installed, but we don't need it since python is avail
FROM cgr.dev/chainguard/python:latest

WORKDIR /app

ENV PYTHONUNBUFFERED=1
# UV put the virutal environment on /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

# copy application files to WORKDIR (/app)
COPY main.py /app

# bring in the virtual environment / packages from the builder directory
COPY --from=builder /app/.venv /app

# run line for app
ENTRYPOINT [ "python","/app/main.py" ]

# ----- OLD python base version

# FROM cgr.dev/chainguard/python:latest-dev as builder

# ENV LANG=C.UTF-8
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1
# ENV PATH="/app/venv/bin:$PATH"

# # use /app generic folder
# WORKDIR /app

# # use python venv to bring in any necessary packages
# RUN python -m venv /app/venv
# COPY requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt

# FROM cgr.dev/chainguard/python:latest

# WORKDIR /app

# ENV PYTHONUNBUFFERED=1
# ENV PATH="/venv/bin:$PATH"

# # copy application files to WORKDIR (/app)
# COPY linky.py linky.png ./
# # bring in the packages from requirements.txt
# COPY --from=builder /app/venv /venv

# # run line for app
# # ENTRYPOINT [ "python", "/app/linky.py" ]
# ENTRYPOINT [ "waitress-serve" ]