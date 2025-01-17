# Base Image from python, supaya mudah dalam menggunakan setiap librarynya
FROM ultralytics/ultralytics:latest

WORKDIR /app

# Install Python and dependencies
RUN \
    apt-get update -y && \
    apt-get install -y wget && \
    cd /usr/src/ultralytics/ultralytics/engine && \
    wget -O exporter.py https://raw.githubusercontent.com/ultralytics/ultralytics/main/ultralytics/engine/exporter.py
#COPY requirements.txt .
#RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "inference_CLI.py"]