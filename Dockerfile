FROM python:3.8-alpine
LABEL author="bugre"
LABEL name="my_hello_world"

RUN mkdir /app
ADD my_hello_world.py /app/


WORKDIR /app

CMD ["python", "my_hello_world.py"]