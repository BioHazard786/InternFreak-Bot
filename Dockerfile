FROM ubuntu:latest

RUN apt update && apt upgrade -y
RUN DEBIAN_FRONTEND="noninteractive" apt install git python3 python3-pip -y 
RUN pip3 install -U pip

RUN mkdir /app/
WORKDIR /app/
RUN chmod 777 /app/
COPY . /app/
EXPOSE 8000

RUN pip3 install -U -r requirements.txt
CMD ["python3", "-m", "InternFreak"]