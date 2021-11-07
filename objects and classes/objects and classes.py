#make 2 programs using objects
class basket:
    def __init__(fruits,name,cost):
        fruits.name=name
        fruits.cost=cost
    def list(fruits):
        print(fruits.name,"=",fruits.cost)
p1=basket('mangoes','14 rupees')
p1.list()

class bowl:
    def __init__(basket,name,cost):
        basket.cost=cost
        basket.name=name
    def see(basket):
        print(basket.name,"=",basket.cost)
p2=bowl('mangooes','14')
p2.see()