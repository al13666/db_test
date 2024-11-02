FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    nginx \
    curl \
	postgresql \
	python3 \
	python3-pip \
    && rm -rf /var/lib/apt/lists/*

#RUN apt-get install -y libpq

RUN python3 -m pip install flask --break-system-packages

RUN python3 -m pip install psycopg2-binary --break-system-packages



WORKDIR /Server

COPY . /Server

#CMD ["nginx", "-g", "daemon off;"]
CMD python3 service.py
