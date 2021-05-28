FROM python

WORKDIR /app

RUN pip3 install fastapi
RUN pip3 install uvicorn[standard]
RUN pip3 install Pillow
RUN pip3 install tensorflow-cpu
RUN pip3 install numpy

# ENV CUDA_VISIBLE_DEVICES="-1"

COPY . /app

EXPOSE 8000
CMD ["uvicorn", "main:app"]
