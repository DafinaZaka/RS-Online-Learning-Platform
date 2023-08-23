FROM python:3.9

EXPOSE 8501
EXPOSE 8502

WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt



COPY . .
RUN chmod +x start.sh
CMD ["./start.sh"]