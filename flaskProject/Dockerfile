# Docker image for flask python run
# VERSION 1.0
# Author: Weiye
# 基础镜像使用python:3.7
FROM python:3.7
# 将服务器 requirements.txt 文件复制到 容器 /project/目录下
COPY requirements.txt /project/
# 指定容器工作目录为 /project/
WORKDIR /project/
# 安装 项目依赖
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
# 运行
ENTRYPOINT ["python","app.py"]

# 编译
# docker build -t weiye/flask-project:v1 .

# run
#docker run -it -p 7090:7090 --name flask-project \
#-v /mydata/flaskProject:/project \
#-d weiye/flask-project:v1