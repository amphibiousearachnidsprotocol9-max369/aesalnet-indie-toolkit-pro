                    FROM python:3.11-slim

WORKDIR /app

COPY src ./src
COPY dashboards ./dashboards
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "dashboards.status_dashboard"]
