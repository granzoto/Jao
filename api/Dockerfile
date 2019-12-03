FROM python:3.6

# Definir a porta correta para a a API
EXPOSE 5000

# Diretorio onde a API roda
WORKDIR /api

# Instalar os requerimentos, caso existam, via PIP 
COPY requirements.txt /api
RUN pip install -r requirements.txt

# Roda a API 
COPY api.py /api
CMD python api.py
