import json
from random import randint, choice
from pprint import pprint
  
def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)

def read(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

class Coffe:
    def __init__(self):
        self.ml = randint(150, 400)
        self.type = choice(['Espresso', 'Doppio', 'Tripplo', 'Ritretto', 'Lungo', 'Mocha', 'Glace', 'Irish', 'Cappuccino', 'Latte', 'Macchiato', 'Romano'])
        self.amount = randint(1, 31)

data = {
    'Coffe': []
}

for i in range(50):
    data['Coffe'].append(Coffe().__dict__)

n_data = read('data_lab2.json')
print(n_data['Coffe'][49])
g = Coffe()

g.name = n_data['Coffe'][4]['type']

print(g.name)

input()


#========================================================REPLY======================================================================
#C:\Users\svape\PycharmProjects\pythonProject\venv\Scripts\python.exe "C:\Users\svape\PycharmProjects\pythonProject\lab2_for_K;).py" 
#{'ml': 400, 'type': 'Latte', 'amount': 1}
#Latte
