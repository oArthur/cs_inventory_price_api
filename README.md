# Inventory Value Steam API

## Overview
A Inventory Value API é uma aplicação FastAPI projetada para calcular o valor total do inventário de skins de CSGO de um usuário na plataforma Steam. Esta API coleta todas as skins do usuário, verifica o valor de mercado de cada uma na Steam e retorna um resumo em formato JSON, incluindo a quantidade de skins comercializáveis, o valor de cada skin e o valor total do inventário.

## Motivação
Esta API foi desenvolvida para ajudar um amigo que possui uma vasta coleção de skins no Steam e desejava ter uma visão clara do valor total de seu inventário. A Steam não fornece uma funcionalidade que agregue o valor total das skins, fornecendo apenas o valor individual de cada item. Assim, surgiu a necessidade de criar uma solução que simplificasse essa tarefa.

## Recursos
- **Consulta de Inventário**: Obtenha detalhes de todas as skins do inventário de um usuário do Steam.
- **Avaliação de Mercado**: Verifique o valor atual de mercado de cada skin na Steam.
- **Resumo do Inventário**: Receba um relatório detalhado do inventário, incluindo o número total de skins comercializáveis, o valor individual e o valor total do inventário.

## Como Usar
Para começar a usar a Inventory Value API, siga os passos abaixo:

1. Clone o repositório: git clone: `https://github.com/oArthur/cs_inventory_price_api.git`
2. Navegue até o diretório do projeto: `cd cs_api` 
3. Instale as dependências necessárias: `pip install -r requirements.txt`
4. Inicie o servidor: `uvicorn app:main --reload`



Acesse `http://localhost:8000/docs` para ver a documentação interativa da API e testar os endpoints.

## Endpoints
- `GET /inventory/{user_id}`: Retorna o valor total e detalhes do inventário do usuário especificado.

## Exemplo Resposta Json

```json
{
    "inventory": {
        "steam_id": 76561197965130430,
        "total_skins": 17,
        "valor_skins": 6.69,
        "skins_list": [
            {
                "skin_name": "Sticker | OG | Paris 2023",
                "price": "R$ 0,04"
            },
            {
                "skin_name": "Sticker | paiN Gaming | Paris 2023",
                "price": "R$ 0,04"
            },
            {
                "skin_name": "Sticker | Apeks | Paris 2023",
                "price": "R$ 0,07"
            },
            {
                "skin_name": "Sticker | forZe eSports | Paris 2023",
                "price": "R$ 0,03"
            },
            {
                "skin_name": "Sticker | Monte | Paris 2023",
                "price": "R$ 0,08"
            },
            {
                "skin_name": "Sticker | BLAST.tv | Paris 2023",
                "price": "R$ 0,01"
            },
            {
                "skin_name": "Sticker | G2 Esports | Paris 2023",
                "price": "R$ 0,05"
            },
            {
                "skin_name": "Sticker | Ninjas in Pyjamas | Paris 2023",
                "price": "R$ 0,02"
            },
            {
                "skin_name": "Sticker | G2 Esports (Glitter) | Paris 2023",
                "price": "R$ 0,82"
            },
            {
                "skin_name": "Sticker | paiN Gaming (Glitter) | Paris 2023",
                "price": "R$ 0,55"
            },
            {
                "skin_name": "Sticker | BLAST.tv (Glitter) | Paris 2023",
                "price": "R$ 0,05"
            },
            {
                "skin_name": "Sticker | GamerLegion (Glitter) | Paris 2023",
                "price": "R$ 0,42"
            },
            {
                "skin_name": "Sticker | Bad News Eagles | Paris 2023",
                "price": "R$ 0,02"
            },
            {
                "skin_name": "Sticker | Fnatic | Paris 2023",
                "price": "R$ 0,04"
            },
            {
                "skin_name": "Sticker | Heroic | Paris 2023",
                "price": "R$ 0,02"
            },
            {
                "skin_name": "Sticker | FURIA | Paris 2023",
                "price": "R$ 0,02"
            },
            {
                "skin_name": "USP-S | Lead Conduit (Field-Tested)",
                "price": "R$ 4,41"
            }
        ]
    }
}
```

## Contribuições
Contribuições são bem-vindas! Se você tiver sugestões de melhorias ou encontrar bugs, sinta-se à vontade para abrir uma issue ou enviar um pull request.


