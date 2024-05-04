def enqueue(queue,item):
    queue.append(item)

def dequeue(queue):
    return queue.pop(0)
    
def peek(queue):
    return queue[0]

def isempty(queue):
    return len(queue) == 0
    
def size(queue):
    return len(queue)

pizzaqueue = []

enqueue(pizzaqueue,"pizza hawaii")
enqueue(pizzaqueue,"pizza calzone")
enqueue(pizzaqueue,"pizza calzone")

print('Eerstvolgende aan de beurt: ' + peek(pizzaqueue))
print(str(size(pizzaqueue)) + ' pizza''s in de wachrij')

#Opdracht herschrijf onderstaande lijnen in een while loop
currentpizza = dequeue(pizzaqueue)
print(currentpizza + ' aan het klaarmaken')
sleep(2)

currentpizza = dequeue(pizzaqueue)
print(currentpizza + ' aan het klaarmaken')
sleep(2)

currentpizza = dequeue(pizzaqueue)
print(currentpizza + ' aan het klaarmaken')
sleep(2)
