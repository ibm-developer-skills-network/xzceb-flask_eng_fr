FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 7777
ENTRYPOINT [ "python" ]
CMD [ "server.py" ]