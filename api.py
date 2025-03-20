from abc import ABCMeta, abstractmethod
import requests

class API_consumer(metaclass=ABCMeta):
    @abstractmethod
    def extract(self, id):
        pass


class API_Pokemon(API_consumer):
    def __init__(self):
        self.__URL = 'https://pokeapi.co/api/v2/pokemon/'

    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
        URL = self.URL + str(id)
        try:
            dado = requests.get(URL).json()
            return ((dado.get('id'), dado.get('name')))
        except:
            pass

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

    
    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
    # Atividade 3, que resultará o segundo commit
        pass

class API_Star_Wars(API_consumer):
    ''' The universe of Star Wars '''
    def __init__(self):
        self.__URL = 'https://swapi.dev/api/people/'

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
    
    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
    # Atividade 4, que resultará o terceiro commit
        pass

class API_Ice_and_Fire(API_consumer):
    ''' The universe of Ice And Fire '''
    def __init__(self):
        self.__URL = 'https://anapioficeandfire.com/api/characters/'

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
    
    @property
    def URL(self):
        return self.__URL

    def extract(self, id):
        # Atividade 5, que resultará o quarto commit
        pass
 