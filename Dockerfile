#Python version
FROM python:3.10-slim 

WORKDIR /app

COPY requeriments.txt .

RUN pip install --no-cache-dir -r requeriments.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
