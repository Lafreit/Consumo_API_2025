Primeiro commit
api.py
main.py

Instalando o ambiente virtual:
no prompt de comando do sistema operacional do windows:
1) Criação do ambiente virtual:
Abra seu terminal ou prompt de comando.
Navegue até a pasta onde deseja criar o ambiente virtual.
Execute o comando abaixo para criar o ambiente virtual:
python -m venv consumo_api_2025
2) Ativação do ambiente virtual:
consumo_api_2025\Scripts\activate
3) Instalação da biblioteca request:
pip install requests
4) Verificação da instalação:
Para garantir que a biblioteca foi instalada corretamente, use o comando:
pip list
Isso mostrará todas as bibliotecas instaladas no ambiente virtual, incluindo o requests.


Criação da class API_Rick_Morty.

class API_Rick_Morty:
    def __init__(self):
        self.base_url = "https://rickandmortyapi.com/api/character/"

    def extract(self, id):
        try:
            # 3.1 Concatenar o ID à URL base
            endpoint = f"{self.base_url}{id}"

            # 3.2 Fazer uma requisição GET para obter os dados
            response = requests.get(endpoint)
            response.raise_for_status()  # Levanta um erro se o status não for 200
            data = response.json()

            # 3.3 Retornar uma tupla contendo (id, name, species)
            return (data['id'], data['name'], data['species'])

        except requests.exceptions.RequestException as e:
            # 3.4 Tratar exceções relacionadas à requisição
            print(f"Erro na requisição: {e}")
            return None
        except KeyError as e:
            # Tratar exceções caso a chave não exista
            print(f"Erro ao acessar dados: {e}")
            return None

Explicação dos passos:
URL Base + ID: O método concatena o id com a URL base para formar o endpoint correto.
Requisição GET: Utiliza o módulo requests para enviar a requisição e obter os dados no formato JSON.
Tupla (id, name, species): Extrai as informações específicas do personagem e retorna como tupla.
Tratamento de Exceções: Utiliza try-except para evitar que falhas na requisição ou erros nos dados recebidos quebrem o programa.

URL Base + ID; Requisição GET; Tupla; Tratamento de Exceções.

Implementação da class API_Star_Wars:

class API_Star_Wars:
    def __init__(self):
        self.base_url = "https://swapi.dev/api/people/"

    def extract(self, id):
        try:
            # 4.1 Concatenar o ID à URL base para formar o endpoint
            endpoint = f"{self.base_url}{id}/"

            # 4.2 Fazer uma requisição GET para obter os dados JSON
            response = requests.get(endpoint)
            response.raise_for_status()  # Lança um erro se o status HTTP não for 200
            data = response.json()

            # 4.3 Extrair o nome e a lista de filmes
            name = data['name']
            films = data['films']  # Lista de URLs de filmes

            # Retorna uma tupla contendo o nome e a lista de filmes
            return (name, films)

        except requests.exceptions.RequestException as e:
            # 4.4 Tratar exceções relacionadas à requisição
            print(f"Erro na requisição: {e}")
            return None
        except KeyError as e:
            # Tratar exceções caso alguma chave não exista
            print(f"Erro ao acessar dados: {e}")
            return None
Detalhes da implementação:
URL Base + ID: Concatenamos o id à URL base (https://swapi.dev/api/people/) para formar o endpoint correto.
Requisição GET: Utilizamos a biblioteca requests para fazer a requisição e obtemos os dados no formato JSON.
Nome e Filmes: Extraímos o campo name (nome do personagem) e films (lista de URLs dos filmes em que ele aparece).
Tratamento de Exceções:
Lidamos com erros de requisição (conexão, timeout, status HTTP inválido).
Lidamos com possíveis chaves ausentes nos dados retornados pela API.

lass API_Star_Wars
URL Base + ID; Requisição GET; Nome e Filmes; Tratamento de Exceções


Criando a class API_Ice_and_Fire:

class API_Ice_and_Fire:
    def __init__(self):
        self.base_url = "https://anapioficeandfire.com/api/characters/"

    def extract(self, id):
        try:
            # 5.1 Concatenar o ID à URL base para formar o endpoint
            endpoint = f"{self.base_url}{id}"

            # 5.2 Fazer uma requisição GET para obter os dados JSON
            response = requests.get(endpoint)
            response.raise_for_status()  # Lança um erro caso o status HTTP não seja 200
            data = response.json()

            # 5.3 Extrair o nome e as séries de TV relacionadas ao personagem
            name = data['name'] if data['name'] else "Desconhecido"
            tv_series = data['tvSeries'] if data['tvSeries'] else []

            # Retorna uma tupla contendo o nome e a lista de séries de TV
            return (name, tv_series)

        except requests.exceptions.RequestException as e:
            # 5.4 Tratar exceções relacionadas à requisição
            print(f"Erro na requisição: {e}")
            return None
        except KeyError as e:
            # Tratar exceções caso alguma chave esteja ausente
            print(f"Erro ao acessar dados: {e}")
            return None
Detalhes da implementação:
URL Base + ID: O ID do personagem é concatenado à URL base da API de "A Song of Ice and Fire" para criar o endpoint correto.
Requisição GET: Utiliza-se o módulo requests para fazer a requisição e processar os dados no formato JSON.
Tupla (name, tvSeries):
O campo name armazena o nome do personagem. Se ele estiver vazio, um valor padrão como "Desconhecido" é usado.
O campo tvSeries é retornado como uma lista, contendo os nomes das séries relacionadas ao personagem.
Tratamento de Exceções:
Problemas na requisição (conexão, timeout, ou falhas HTTP) são tratados com mensagens informativas.
Chaves ausentes nos dados JSON também são protegidas para evitar que o programa quebre.

class API_Ice_and_Fire
URL Base + ID; Requisição GET; Tupla; O campo name armazena o nome do personagem; Tratamento de Exceções

