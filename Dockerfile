FROM raspbian/stretch

WORKDIR /app
COPY . /app

RUN apt-get update
RUN apt-get install -y \
    python3-minimal \
    python3-pip \
    vim

RUN export LC_ALL=C.UTF-8 && export LANG=C.UTF-8

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt

RUN ln -s /usr/bin/python3 /usr/bin/python && ln -s /usr/bin/pip3  /usr/bin/pip