FROM python:latest

WORKDIR /app

COPY /stage_3/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY /stage_log /app/stage_log

COPY /stage_3 /app/stage_3

CMD ["python", "-m" , "stage_3.main"]