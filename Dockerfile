FROM python:2-alpine
COPY restgap.py /root/
RUN pip install flask flask-cors
ENV FLASK_APP=restgap
WORKDIR /root/
CMD flask run --host=0.0.0.0
EXPOSE 5000
