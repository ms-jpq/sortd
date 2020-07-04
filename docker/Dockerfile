FROM python:latest


COPY . /
RUN pip install -U mypy
RUN pip install -U -r requirements.txt
RUN ./lint.sh
RUN ./slines < ./tests/txt.txt
RUN ./sjson < ./tests/json.json
RUN ./syaml < ./tests/yaml.yaml
RUN ./stoml < ./tests/toml.toml
