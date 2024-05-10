FROM python:3.9-slim-buster

WORKDIR /python-docker

COPY ./app/requirements.txt requirements.txt

# Update pip
RUN pip install --upgrade pip

# Install HDF5 using apt
RUN apt-get update && apt-get install -y libhdf5-dev pkg-config gcc

RUN pip3 install -r requirements.txt

COPY ./app .
COPY ./model.h5 .

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]