FROM node:24.4.0-alpine AS frontend-build

WORKDIR /usr/src/app

COPY ./frontend/package.json ./
COPY ./frontend/package-lock.json ./

RUN npm ci && npm cache clean --force

COPY ./frontend/ .

RUN npm run build

FROM python:3.11.5-alpine

WORKDIR /app

COPY backend/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ .

COPY --from=frontend-build /usr/src/app/dist/ /frontend/dist

ENV API_KEY="${API_KEY}"

ENV ASSETS_DIR="${ASSETS_DIR}"

ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4" , "main:app" ]