FROM python:latest
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5002
CMD [ "python","app.py" ]