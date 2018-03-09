FROM python:3.5
LABEL mainter="Jappie Klooster"
EXPOSE 8080

COPY src /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD [ "python", "./run.py"]
