import random
import pyinputplus as pyip
from pprint import pprint

def get_datas(nums:int) -> list[str]:
    with open('names.txt',encoding='utf-8') as file:
        content:str = file.read()
        datas:list[str] = content.split(sep='\n')
        random_datas:list[str] = random.choices(datas,k=nums)
    return random_datas

#############################################################
def get_sources(datas:list[str]) -> list[dict]:
    peoples:list[dict] = []
    for data in datas:
        people:dict[str:any] = {}
        people["name"] = data
        people["height"] = random.randint(150,220)
        people["weight"] = random.randint(40,90)
        peoples.append(people)
    return peoples

##############################################################

def main():
    numbers:int = pyip.inputInt("請輸入人數(1~50):",min=1,max=50)
    datas:list[str] = get_datas(nums=numbers)
    peopleData:list[dict] = get_sources(datas)
    pprint(peopleData)

main()