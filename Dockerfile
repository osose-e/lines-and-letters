FROM python:3.12

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

# Cloud Run sets PORT at runtime; app.py reads it. Use python so we bind to 0.0.0.0:PORT.
ENV PORT=8080
CMD ["python", "app.py"]