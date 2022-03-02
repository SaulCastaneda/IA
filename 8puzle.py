from copy import deepcopy
import numpy as np
import time
# Algoritmo de busqueda  Manhantthan 

# Scanner de Estados
def bestsolution(state):
    bestsol = np.array([], int).reshape(-1, 9)
    count = len(state) - 1
    while count != -1:
        bestsol = np.insert(bestsol, 0, state[count]['puzzle'], 0)
        count = (state[count]['parent'])
    return bestsol.reshape(-1, 3, 3)

       
# esta función verifica la union del estado de la iteración, ya sea que haya sido atravesado previamente o no.
def all(checkarray):
    set=[]
    for it in set:
        for checkarray in it:
            return 1
        else:
            return 0


#calcula el costo de la distancia de Manhattan entre cada dígito del rompecabezas (estado inicial) y el estado objetivo
def manhattan(puzzle, goal):
    a = abs(puzzle // 3 - goal // 3)
    b = abs(puzzle % 3 - goal % 3)
    mhcost = a + b
    return sum(mhcost[1:])




# calculará el número de fichas extraviadas en el estado actual en comparación con el estado objetivo
def misplaced_tiles(puzzle,goal):
    mscost = np.sum(puzzle != goal) - 1
    return mscost if mscost > 0 else 0
       


def coordinates(puzzle):
    pos = np.array(range(9))
    for p, q in enumerate(puzzle):
        pos[q] = p
    return pos



#  Manhattan Distance
def evaluvate(puzzle, goal):
    steps = np.array([('up', [0, 1, 2], -3),('down', [6, 7, 8],  3),('left', [0, 3, 6], -1),('right', [2, 5, 8],  1)],
                dtype =  [('move',  str, 1),('position', list),('head', int)])

    dtstate = [('puzzle',  list),('parent', int),('gn',  int),('hn',  int)]
    
    
    costg = coordinates(goal)
    parent = -1
    gn = 0
    hn = manhattan(coordinates(puzzle), costg)
    state = np.array([(puzzle, parent, gn, hn)], dtstate)

# Prioridad
    dtpriority = [('position', int),('fn', int)]
    priority = np.array( [(0, hn)], dtpriority)



    while 1:
        priority = np.sort(priority, kind='mergesort', order=['fn', 'position'])     
        position, fn = priority[0]                                                 
        priority = np.delete(priority, 0, 0)                    
        puzzle, parent, gn, hn = state[position]
        puzzle = np.array(puzzle)
        blank = int(np.where(puzzle == 0)[0])       
        gn = gn + 1                              
        c = 1
        start_time = time.time()
        for s in steps:
            c = c + 1
            if blank not in s['position']:
                # genera un nueva copia del estado
                openstates = deepcopy(puzzle)                   
                openstates[blank], openstates[blank + s['head']] = openstates[blank + s['head']], openstates[blank]             
                if ~(np.all(list(state['puzzle']) == openstates, 1)).any():    
                    end_time = time.time()
                    if (( end_time - start_time ) > 2):
                        print(" El 8 puzzle no Tiene Solucion ! \n")
                        exit 
                    
                    hn = manhattan(coordinates(openstates), costg)    
                   #Genera un nuevo estado y lo copia                  
                    q = np.array([(openstates, position, gn, hn)], dtstate)         
                    state = np.append(state, q, 0)
                    # FN son los costo de moviemento
                    fn = gn + hn                                        
            
                    q = np.array([(len(state) - 1, fn)], dtpriority)    
                    priority = np.append(priority, q, 0)
                      #Valida si la convinacion de estados tiene solucion
                    if np.array_equal(openstates, goal):                              
                        print(' EL 8 puzzle Tiene Solucion :D ! \n')
                        return state, len(priority)
        
                        
    return state, len(priority)


#Mpisplaced tiles



# ----------  FUNCION MAIN -----------------


puzzle = []
print(" Ingresa el estado Inicia ")
for i in range(0,9):
    x = int(input("Ingresa los valores :"))
    puzzle.append(x)

      
goal = []
print(" ingresa los valores de 0-8 para el estado de la meta ")
for i in range(0,9):
    x = int(input("Ingresa los valores :"))
    goal.append(x)



n = int(input("1. Manhattan distance \n2. Misplaced tiles "))

if(n ==1 ): 
    state, visitado = evaluvate_misplaced(puzzle, goal) 
    bestpath = bestsolution(state)
    print(str(bestpath).replace('[', ' ').replace(']', ''))
    totalmoves = len(bestpath) - 1
    print('pasos a encontrar la Solucion:',totalmoves)
    visit = len(state) - visitado
    print('Total nodos visitados: ',visit, "\n")
    print('Total movientos generados:', len(state))    
