import time

def enqueue(queue,item):
    queue.append(item)

def dequeue(queue):
    return queue.pop(0)

def isempty(queue):
    return len(queue) == 0
    
def size(queue):
    return len(queue)

pizzaqueue = []

enqueue(pizzaqueue,"pizza hawaii")
enqueue(pizzaqueue,"pizza calzone")
enqueue(pizzaqueue,"pizza calzone")

print(str(size(pizzaqueue)) + ' pizza''s in de wachrij')

#Opdracht 1 schrijf een functie om één pizza klaar te maken
#           met als parameter de pizzaqueue en gebruik dan de 
#           functie om onderstaande drie blokken te herschrijven in één lijn
#           Kies een gepaste naam voor de functie

currentpizza = dequeue(pizzaqueue)
print(currentpizza + ' aan het klaarmaken')
time.sleep(2)

currentpizza = dequeue(pizzaqueue)
print(currentpizza + ' aan het klaarmaken')
time.sleep(2)

currentpizza = dequeue(pizzaqueue)
print(currentpizza + ' aan het klaarmaken')
time.sleep(2)

#Opdracht 2 herschrijf de drie lijnen in een loop
#           denk na of je een for of een while gebruikt
