# Questão 14 — Container para um Script de Processamento

FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*


WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY process.py .

CMD ["python3", "process.py"]