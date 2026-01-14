import logging
from pathlib import Path
from random import choice

import requests
from faker import Faker

fake = Faker("pt_BR")
# Define como faremos o log das ações
logging.basicConfig()
logger = logging.getLogger("lactec.intranet.popula")
logger.setLevel(logging.INFO)


# Constantes utilizadas no script
PASTA_ATUAL = Path(__file__).parent.resolve()
PASTA_DADOS = PASTA_ATUAL / "data"
BASE_URL = "http://localhost:8080/Plone/++api++"
USUARIO = "admin"
SENHA = "admin"

TOTAL_COLABORADORES = 1000
CARGOS = ["clt", "terceiro"]

# Cabeçalhos HTTP
headers = {"Accept": "application/json"}

session = requests.Session()
session.headers.update(headers)

# Autenticar o usuário admin utilizando um Token JWT
login_url = f"{BASE_URL}/@login"
response = session.post(login_url, json={"login": USUARIO, "password": SENHA})
data = response.json()
token = data["token"]
session.headers.update({"Authorization": f"Bearer {token}"})

ENDERECO = {
    "endereco": "Praça Edgar Nogueira, 80 ",
    "complemento": "",
    "cidade": "Curitiba",
    "estado": "PR",
    "cep": "80220-902",
}

AREAS = {
    "/estrututura": {
        "id": "estrututura",
        "@type": "Document",
        "title": "Áreas",
        "description": "Áreas da Lactec",
    },
    "/colaboradores": {
        "id": "colaboradores",
        "@type": "Document",
        "title": "Colaboradores",
        "description": "Colaboradores da Lactec",
    },
    "/estrututura/ascom": {
        "id": "ascom",
        "@type": "Area",
        "title": "ASCOM",
        "description": "Assessoria de Comunicação",
        "telefone": "6132410123",
        "email": "secom@lactec.com.br",
    },
    "/estrututura/sti": {
        "id": "sti",
        "@type": "Area",
        "title": "STI",
        "description": "Secretaria de Tecnologia de Informação",
        "telefone": "6132410123",
        "email": "sti@lactec.com.br",
    },
    "/estrututura/sti/web": {
        "id": "web",
        "@type": "Area",
        "title": "Desenvolvimento Web",
        "description": "Secretaria de Tecnologia de Informação - Web",
        "telefone": "6132410123",
        "email": "sti-web@lactec.com.br",
    },
}

# Criar Áreas

for path in AREAS:
    data = AREAS[path]
    parent_path = "/".join(path.split("/")[:-1])[1:]
    response = session.get(f"{BASE_URL}/{path}")
    if response.status_code != 404:
        area = response.json()
        AREAS[path]["UID"] = area["UID"]
        logger.info(f"Ignorando {BASE_URL}{path}: Conteúdo já existe")
        continue
    if data["@type"] == "Area":
        data.update(ENDERECO)
    response = session.post(f"{BASE_URL}/{parent_path}", json=data)
    if response.status_code > 300:
        logger.error(f"Erro ao criar '{path}': {response.status_code}")
    else:
        logger.info(f"Conteúdo criado: '{path}'")
        area = response.json()
        AREAS[path]["UID"] = area["UID"]


areas = [area["UID"] for area in AREAS.values() if area["@type"] == "Area"]
parent_url = f"{BASE_URL}/colaboradores"
idx = 1
while idx < 1000:
    area = choice(areas)
    profile = fake.profile()
    username = profile["username"]
    cargo = choice(CARGOS)
    data = {
        "id": f"{username}",
        "@type": "Pessoa",
        "title": profile["name"],
        "description": profile["job"],
        "cargo": cargo,
        "area": area,
        "telefone": f"6132130{idx:03d}",
        "email": f"{username}@lactec.com.br",
    }
    data.update(ENDERECO)
    path = data["id"]
    response = session.get(f"{parent_url}/{path}")
    if response.status_code != 404:
        logger.info(f"Ignorando {parent_url}/{path}: Conteúdo já existe")
        continue
    response = session.post(parent_url, json=data)
    if response.status_code > 300:
        logger.error(f"Erro ao criar '{path}': {response.status_code}")
    else:
        logger.info(f"Conteúdo criado: '{path}'")
        idx += 1
