FROM python:3.8-slim
WORKDIR /app

# requirements and dependencies
RUN pip install psycopg2-binary
RUN pip install pandas

RUN mkdir -p ./data
RUN mkdir -p ./processed_data

COPY load.py .
COPY extract_transform.py .
COPY data/ ./data/

CMD ["python", "unit_test2.py"]