FROM python:2.7-slim as build

RUN mkdir /install
WORKDIR /install
RUN     /usr/local/bin/python -m pip install --upgrade pip &&\
		pip install lac uniout \
        --prefix="/install"\
        -i https://mirror.baidu.com/pypi/simple

FROM python:2.7-slim 
COPY --from=build /install /usr/local
COPY . ~/app
RUN 	apt-get update &&\
		apt-get install libgomp1
WORKDIR ~/app

CMD [ "python", "main.py" ]
