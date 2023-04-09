FROM python:3.9-slim-buster
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ENV PATH="/usr/local/bin:${PATH}"
CMD ["python", "app.py"]