FROM python:3.12-slim

ARG APP_VERSION=1.0.0
ARG GIT_COMMIT=unknown
ARG GIT_REPO=https://github.com/ahmedhanbal/student-ml-api
ARG BUILD_DATE=unknown

LABEL org.opencontainers.image.title="student-ml-api" \
      org.opencontainers.image.version="${APP_VERSION}" \
      org.opencontainers.image.revision="${GIT_COMMIT}" \
      org.opencontainers.image.source="${GIT_REPO}" \
      org.opencontainers.image.created="${BUILD_DATE}"

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Copy and install dependencies first so later app.py-only changes reuse this layer.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Application files change more often than dependencies.
COPY app.py VERSION ./

EXPOSE 5000

CMD ["python", "app.py"]
