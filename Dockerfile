FROM python:3.10.3-slim

RUN useradd lab_manager

WORKDIR /home/lab_manager

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn pymysql cryptography

COPY lab_manager lab_manager
COPY migrations migrations
COPY app.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP app.py

RUN chown -R lab_manager:lab_manager ./
USER lab_manager

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]