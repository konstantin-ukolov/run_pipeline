FROM python:3.9-slim-buster
WORKDIR /app

RUN pip install pytelegrambotapi
COPY run_pipeline_bot.py .

CMD ["python", "run_pipeline_bot.py"]