import json

def Arc_consistency(nodos, constraints, domain, assignments,arcs):
    #fill queue with initial arcs
    fillQueue(nodos,constraints,arcs)
    while arcs:
        arcVars = arcs.pop(0)
        if Domain_Touched(arcVars[0], arcVars[1], nodos, constraints, domain, assignments, arcs):
            domainIIndex = nodos.index(arcVars[0])
            if len(domain[domainIIndex]) == 0:
                print ("No Solution")
                return False
            neighbors = list(constraints[domainIIndex])
            neighbors.remove(arcVars[1])
            for xk in neighbors:
                arcs.append([xk, arcVars[0]])
    return assignments


#fill queue with initial arcs
def fillQueue(nodos,constraints,arcs):
    for var in nodos:
        varIndex = nodos.index(var)
        for arc in constraints[varIndex]:
            arcs.append([var, arc])

def Domain_Touched( Xi, Xj, nodos, constraints, domain, assignments,arcs):
    touched = False
    Iindex = nodos.index(Xi);
    #for each value in the domain
    for x in domain[Iindex]:
        #check if state is adjacent, if not, go to next x
        if Xj not in constraints[Iindex]:
            break
        if Xj not in assignments:
            continue
        #if adjacent state has current assignment of X (same color)
        if x in assignments[Xj]:
            domain[Iindex].remove(x)  #remove x from Di
            touched = True
    if not touched and len(domain[Iindex]) > 0:
        assignments[Xi] = domain[Iindex][0]
    return touched

def main():
    isInter = False
    nodos = []
    constraints = []
    domain = []
    aux = []
    aux1= []
    dias=["L","M","Mi","J","V"]
    salas=["A","B","C"]
    assignments = { }
    arcs = []
    count = 0
    for i in range(0, 1): #Se crea el grafo para los dias de la semana
        for x in range(1,7):
            for z in range(0,3):
                nodos.append(dias[i]+"_"+str(x)+"_"+salas[z])  
    for i in range (0,len(nodos)):
        if ('A' in nodos[i]):
            for x in range (1, 4):
                if i == 0:
                    continue
                else:
                    aux.append(nodos[i-x])
            for x in range (1, 6):
                if i+x == len(nodos):
                    break
                else:
                    aux.append(nodos[i+x])
        if ('B' in nodos[i]):
            for x in range (1, 5):
                if i - x == 0:
                    aux.append(nodos[i - x])
                    break
                else:
                    aux.append(nodos[i-x])
            for x in range (1, 5):
                if i + x == len(nodos):
                    break
                else:
                    aux.append(nodos[i+x])
        if ('C' in nodos[i]):
            for x in range (1, 6):
                if i - x == 0:
                    aux.append(nodos[i - x])
                    break
                else:
                    aux.append(nodos[i-x])
            for x in range (1, 4):
                if i + x == len(nodos):
                    break
                else:
                    aux.append(nodos[i+x])
        constraints.append(aux)
        aux = []      
    with open('charlas.json') as file:
        data = json.load(file)
        for charla in data['charlas']:
            for i in range (0, len(charla['dias_disponibles'])):
                for x in range (0, len(charla['horas_disponibles'])):
                    aux.append(charla['dias_disponibles'] [i] + "_" + str(charla['horas_disponibles'] [x]) + "_" + charla['nacionalidad'] + "_" + charla['nombre'] + "_" + charla['area'])
    for i in range (0, len(nodos)):
        for x in range (0, len(aux)):
            isInter = False
            if nodos[i][:3] == aux[x][:3]:
                if aux1 != [] and (aux[x][3:6] in aux1[0]):
                    isInter=True
                if isInter == False or aux1 == []:
                    if aux1 != []:
                        for a in range (0, len(aux1)):
                            if aux[x][-3:] in aux1[a]:
                                count = count + 1
                        if count == 0:
                           aux1.append(aux[x])
                        count = 0 
                    else:
                        aux1.append(aux[x])
        domain.append(aux1)
        aux1 = []
    for i in range (0, len(domain)):
        if domain[i] != []:
            domain[i].append("null")
            domain[i].append("null1")
    #print (nodos) 
    #print (constraints) 
    #print(domain)

    res = Arc_consistency(nodos, constraints, domain, assignments,arcs)
    print (res)
main()