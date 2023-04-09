FROM python:3.9-slim-buster
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ENV PATH="/usr/local/bin:${PATH}"
EXPOSE 8081
CMD ["python", "app.py"]