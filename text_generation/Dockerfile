FROM python:3.7

EXPOSE 8888

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
COPY server.py /usr/src/app/
COPY model.py /usr/src/app/
COPY modelHandler.py /usr/src/app/

COPY training_checkpoints/checkpoint /usr/src/app/training_checkpoints/
COPY training_checkpoints/ckpt_30.data-00000-of-00001 /usr/src/app/training_checkpoints/
COPY training_checkpoints/ckpt_30.index /usr/src/app/training_checkpoints/

RUN pip install --no-cache-dir -r requirements.txt


ENTRYPOINT ["python3", "server.py"]