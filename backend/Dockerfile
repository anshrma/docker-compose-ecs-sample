FROM python:3.8-alpine
WORKDIR /code
COPY ./ /code/

RUN ls -ltr /code
RUN pip install -r requirements.txt
ENV FLASK_APP hello.py
CMD flask run --host=0.0.0.0
 