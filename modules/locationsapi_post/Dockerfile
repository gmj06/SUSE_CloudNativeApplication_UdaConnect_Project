FROM python:latest


WORKDIR .

COPY requirements.txt requirements.txt


RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 5005

COPY . .

ENTRYPOINT [ "python3", "app/locations_grpc_server.py" ]

