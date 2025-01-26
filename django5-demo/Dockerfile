FROM cgr.dev/chainguard/python:latest-dev as builder

ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/venv/bin:$PATH"

# use /app generic folder
WORKDIR /app

# use python venv to bring in any necessary packages
RUN python -m venv /app/venv
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM cgr.dev/chainguard/python:latest

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PATH="/venv/bin:$PATH"

# copy application files to WORKDIR (/app)
COPY .  ./
# bring in the packages from requirements.txt
COPY --from=builder /app/venv /venv

# run line for app
# ENTRYPOINT [ "python", "manage.py", "runserver" ]
ENTRYPOINT ["waitress-serve"]
CMD ["--host=0.0.0.0", "--port=80", "core.wsgi:application"]