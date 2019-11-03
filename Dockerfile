FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app
ENV ACCESS_TOKEN a9c2fc9e74b8fdf5b61c28393eaee431af3f2c07

VOLUME /usr/src/app
CMD [ "python", "./main.py" ]
