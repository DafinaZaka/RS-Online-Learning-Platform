FROM python:3.9

EXPOSE 8501
EXPOSE 8502

WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt



COPY . .

CMD ["./start.sh"]