FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app

RUN pip3 install Pillow
RUN pip3 install tensorflow-cpu
RUN pip3 install numpy

COPY . /app

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host=0.0.0.0"]
