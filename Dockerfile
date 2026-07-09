FROM python:3.13-slim

WORKDIR /app

COPY website/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh

ENV FLASK_ENV=production

CMD ["./entrypoint.sh"]
