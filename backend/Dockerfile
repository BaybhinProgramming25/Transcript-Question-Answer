FROM python:3.11-slim

WORKDIR /app 

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt 

COPY . . 

EXPOSE 3000 

# Be sure to remove reload when pushing this into production
# Still don't know why we have to use 0.0.0.0 instead of localhost 
CMD [ "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "3000", "--reload"]