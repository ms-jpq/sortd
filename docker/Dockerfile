FROM python:latest


COPY . /
RUN pip install -U pyyaml toml
RUN ./slines < ./tests/txt.txt
RUN ./sjson < ./tests/json.json
RUN ./syaml < ./tests/yaml.yaml
RUN ./stoml < ./tests/toml.toml
