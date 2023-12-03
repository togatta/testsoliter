FROM python:3.9.18
WORKDIR /opt
RUN pip install flask
RUN apt-get install git
RUN git clone https://github.com/togatta/testsoliter.git
EXPOSE 5000
CMD ["python", "testsoliter/test.py"]
