FROM python:3.13-slim

WORKDIR /app

COPY /stage_4/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY /stage_log /app/stage_log

COPY /stage_4 /app/stage_4

CMD ["python", "-m" , "stage_4.main"]