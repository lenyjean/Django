FROM python:3.10
EXPOSE 8000
ENV PYTHONUNBUFFERED=1
WORKDIR /
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY . /

RUN python manage.py makemigrations
RUN python manage.py migrate


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]