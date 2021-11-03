import json

def main():
    isInter = False
    nodos = []
    constraints = []
    domain = []
    aux = []
    aux1= []
    dias=["L","M","Mi","J","V"]
    salas=["A","B","C"]
    for i in range(0, 1):
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
                    aux1.append(aux[x])
                
        domain.append(aux1)
        aux1 = []
    print (domain) 
    print (len(domain)) 
    print(aux[0][3:6])
    print(nodos)
    #print(len(constraints))
    #print(len(nodos))

main()