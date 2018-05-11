FROM python:2.7

# 配置项目路径

RUN mkdir /project
WORKDIR /project
ADD requirements.txt /project

RUN pip install -r requirements.txt

ADD . /project
