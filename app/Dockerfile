FROM python:3.10-alpine
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apk update && apk add --virtual build-dependencies build-base gcc 
RUN  pip install --upgrade pip
RUN python -m pip install numpy --config-settings=setup-args="-Dallow-noblas=true" 
RUN python -m pip install --upgrade langchain[all]

RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run"]
