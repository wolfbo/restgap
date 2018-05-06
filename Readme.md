#restgap

Easy little API dummy to allow front-end devs to mock an api.
You can PUT/POST json to the API and GET/DELETE this data again.

## start
You can run this with docker.

    bash:~/PycharmProjects/restgap$ docker build .
    Sending build context to Docker daemon  21.61MB
    Step 1/7 : FROM python:2-alpine
     ---> 5fdd069daf25
    Step 2/7 : COPY restgap.py /root/
     ---> Using cache
     ---> 1046d0761f03
    Step 3/7 : RUN pip install flask
     ---> Using cache
     ---> fd5e10b7625f
    Step 4/7 : ENV FLASK_APP=restgap
     ---> Using cache
     ---> 37924630ae52
    Step 5/7 : WORKDIR /root/
     ---> Using cache
     ---> 4a981a5ee664
    Step 6/7 : CMD flask run --host=0.0.0.0
     ---> Running in ca28ea22d96f
    Removing intermediate container ca28ea22d96f
     ---> 2942cc1bc780
    Step 7/7 : EXPOSE 5000
     ---> Running in eea7e08ad059
    Removing intermediate container eea7e08ad059
     ---> 01765b8751d4
    Successfully built 01765b8751d4
    
    wolfgang@truerave:~/PycharmProjects/restgap$ docker run -ti -p 5000:5000 01765b8751d4
     * Serving Flask app "restgap"
     * Environment: production
       WARNING: Do not use the development server in a production environment.
       Use a production WSGI server instead.
     * Debug mode: off
     * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
    192.168.178.54 - - [06/May/2018 21:47:31] "GET / HTTP/1.1" 200 -
