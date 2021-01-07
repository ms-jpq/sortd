FROM python:latest

COPY . /
RUN pip install -U -r requirements.txt


RUN ./sortd csv < ./tests/csv.csv
RUN ./sortd json < ./tests/json.json
RUN ./sortd toml < ./tests/toml.toml
RUN ./sortd lines < ./tests/txt.txt
RUN ./sortd yaml < ./tests/yaml.yaml