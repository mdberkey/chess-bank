FROM python:3.7-alpine

# Add sample application
ADD run.py /tmp/run.py
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000

# Run it
ENTRYPOINT ["python", "/tmp/application.py"]
