FROM python:3.6

EXPOSE 5000

WORKDIR /app/the_eye
ENV PYTHONPATH="/app/"

COPY requirements.txt /app/the_eye
RUN pip install PyMySQL
RUN pip install -r requirements.txt

COPY . /app/the_eye
ENTRYPOINT ["/bin/bash", "/app/the_eye/entrypoint.sh"]