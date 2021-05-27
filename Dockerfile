FROM python

RUN pip install fastapi

RUN pip install uvicorn[standard]