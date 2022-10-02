FROM ubuntu:22.04
WORKDIR /app
RUN chmod 777 /app

RUN apt update && apt upgrade -y
RUN apt install git python3-pip -y 
RUN pip3 install -U pip


COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt
CMD python3 -u -m InternFreak