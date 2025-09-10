FROM python:latest

WORKDIR /app

COPY /stage_2/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY /stage_log /app/stage_log

COPY /stage_2 /app/stage_2

CMD ["python", "-m" , "stage_2.main"]