FROM python:latest

# RUN mkdir /backend

# WORKDIR /backend

# COPY requirements.txt requirements.txt
# COPY app/   /backend/app

# RUN pip3 install --upgrade pip
# RUN pip3 install -r requirements.txt
# RUN python3 -m grpc_tools.protoc -I./app --python_out=./app \
#            --grpc_python_out=. ./app/location.proto


WORKDIR .

COPY requirements.txt requirements.txt


RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 5005

COPY . .

ENTRYPOINT [ "python3", "app/locations_grpc_server.py" ]

