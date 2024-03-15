from pydantic import BaseModel
from typing import List
import requests
import re

from database.inventory import get_list_ignorados, add_ignorado


ignore_list = get_list_ignorados()

class Skin(BaseModel):
    skin_name: str
    price: str


class SkinResponse(BaseModel):
    steam_id: int
    total_skins: int
    valor_skins: float
    skins_list: List[Skin]


# meu 76561198292100240
# big inventory 76561198043602884
def get_inventory(user_id: int):
    skin = []
    total = 0
    count = 0
    url_inventory = f"https://steamcommunity.com/inventory/{user_id}/730/2"
    response_get_inventory = requests.get(url_inventory)

    if response_get_inventory.status_code == 200:
        data = response_get_inventory.json()
        skins = [desc['market_hash_name'] for desc in data['descriptions'] if
                 desc['market_hash_name'] not in ignore_list]
        for skin_name in skins:
            response_get_skin_price = requests.get(
                f"https://steamcommunity.com/market/priceoverview/?appid=730&market_hash_name={skin_name}&currency=7")
            res = response_get_skin_price.json()

            print(f"{skin_name} ->", response_get_skin_price.status_code)
            if res is not None and "success" in res:
                if res["success"]:
                    price = res["median_price"]
                    skin.append(Skin(skin_name=skin_name, price=price))
                    to_number = re.findall(r"[\d,]+", price)
                    number = ''.join(to_number).replace(',', '.')
                    total += float(number)
                    count += 1
                else:
                    add_ignorado(skin_name)
        resposta = SkinResponse(steam_id=user_id, total_skins=len(skin), valor_skins=total, skins_list=skin, )
        return resposta
    elif response_get_inventory.status_code == 404:
        return {"message": "Error [404] Not found"}
    elif response_get_inventory.status_code == 429:
        return {"message": "Error [429] Too many requests"}
    else:
        return response_get_inventory.status_code, "Error Internal Server Error"
