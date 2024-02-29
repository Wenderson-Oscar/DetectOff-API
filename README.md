Uma API para detecção de comentários ofensivos utilizando FastAPI e um modelo SVM (Support Vector Machine) dos autores [Vargas et al. (2022)](https://aclanthology.org/2022.lrec-1.777) baseia-se na ideia de uma aplicação capaz de classificar textos (comentários, neste caso) como ofensivos ou não, aprimorando a moderação de conteúdo em plataformas digitais.

### 1. Introdução

Esta seção deve oferecer uma visão geral da API, explicando seu propósito e como ela pode ser utilizada. Inclua uma breve descrição do problema que a API visa resolver, a relevância da detecção automática de comentários ofensivos, referenciando o artigo que inspirou sua implementação.

### 2. Tecnologias Utilizadas

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/FastAPI-51bd9c?style=for-the-badge&logo=fastapi&logoColor=white">
<img src="https://img.shields.io/badge/scikit-learn-3776AB?style=for-the-badge&logo=scikit-learn&logoColor=orange">

### 3. Configuração do Ambiente

#### Instalando as Dependências

```bash
pip install -r requirements.txt 
```

### 4. Uso da API

#### ///////////////////////////// CONSUME API - PREDICT /////////////////////////////

```bash
import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_url = os.getenv("API_URL")
comment = "bOM DIA"

predict_endpoint = os.getenv("PREDICT_ENDPOINT")
data = {
    "text": comment
}

response = requests.post(api_url + predict_endpoint, data=data)

if response.status_code == 200:
    result = response.text
    print(result)
else:
    print("Erro ao fazer a previsão:", response.status_code)

```

#### ///////////////////////////// CONSUME API - DATE /////////////////////////////

```bash
consume_json = requests.get(api_url + '/grafic/nonoffensive_comments')

if consume_json.status_code == 200:
    result = consume_json.text
    print(result)
else:
    print('erro', consume_json.status_code)
```

### 5. Conclusão

Ao concluir o desenvolvimento da API para detecção de comentários ofensivos utilizando FastAPI e um modelo SVM, destacamos a eficácia dessa solução em melhorar a moderação de conteúdo em plataformas digitais. A escolha do modelo SVM, baseada em evidências de pesquisa e implementada com as capacidades robustas do FastAPI, demonstrou ser eficiente na classificação dos comentários, contribuindo significativamente para a criação de ambientes online mais seguros e respeitosos. Este projeto não apenas evidencia o potencial das tecnologias de machine learning em aplicações práticas de moderação de conteúdo, mas também reforça a importância da inovação contínua e da colaboração entre desenvolvedores e pesquisadores para enfrentar os desafios digitais contemporâneos.

### 6. Referências

[HateBR: A Large Expert Annotated Corpus of Brazilian Instagram Comments for Offensive Language and Hate Speech Detection](https://aclanthology.org/2022.lrec-1.777) (Vargas et al., LREC 2022)
