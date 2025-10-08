import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)
print(response)

if response.status_code == 200:
        dados_json = response.json()
        dados_restaurantes = {}
        for item in dados_json:
            nome_restaurante = item["Company"]
            if nome_restaurante not in dados_restaurantes:
                   dados_restaurantes[nome_restaurante] = []

            dados_restaurantes[nome_restaurante].append({
                 "item": item['Item'],
                 "price": item['price'],
                 "description": item['description']
            })
else: 
        print(f'O erro foi {response.status_code}')

for nome_do_restaurante, dados in dados_restaurantes.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo,'w') as arquivo_restaurante:
        json.dump(dados,arquivo_restaurante,indent=4)