#Python version
FROM python:3.10-slim 

WORKDIR /app

COPY requirements.txt .

#Opencv dependencies:
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
