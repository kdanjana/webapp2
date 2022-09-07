FROM python
RUN pip3 install flask
COPY ./app.py /opt/app.py
COPY ./templates/ /opt/templates/
WORKDIR /opt
EXPOSE 8080
ENTRYPOINT FLASK_APP=app.py flask run --host=0.0.0.0 --port=8080

