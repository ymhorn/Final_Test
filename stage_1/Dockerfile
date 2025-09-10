FROM python:3.13-slim

WORKDIR /app

COPY /stage_1/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY /stage_log /app/stage_log

COPY /stage_1 /app/stage_1

CMD ["python", "-m" , "stage_1.main"]