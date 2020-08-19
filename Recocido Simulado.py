#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 16:39:53 2018

@author: David
@author: Eliseo
@author: Fredy

@uaem, cinc
"""

from random import randint
from random import choice
import random
import math
import itertools
from scipy.spatial import distance
import sys
costos = []

"""
La funcion 'girar(x,y,valor):= gira un punto x con referencial y, con dos condiciones:
    si valor=1 el angulo en que girara x sera en sentido horario
    si valor=1 el angulo en que girara x sera en sentido anti-horario
"""
def girar(x, y,valor):
    if valor == 1: # el angulo es positivo
        angulo= (math.pi*(90))/180.0
    else:
        angulo= (math.pi*(-90))/180.0
    punto = []
#    x_prima = ((Xc + ((X - Xc)*math.cos(angulo)) + ((Y - Yc)*math.sin(angulo))))
#    y_prima = ((Yc - (X - Xc)*math.sin(angulo)) + (Y - Yc)*math.cos(angulo))

    x_prima = ((y[0] + ((x[0] - y[0])*math.cos(angulo)) + ((x[1] - y[1])*math.sin(angulo))))
    punto.append(round (x_prima))
    y_prima = ((y[1] - ((x[0] - y[0])*math.sin(angulo)) + ((x[1] - y[1])*math.cos(angulo))))
    punto.append(round(y_prima))
    return punto
    #print ([round(x_prima), round(y_prima)])

"""
La funcion 'omegas(vector)':= determina apartir de un punto(vector) y 
su direccion del vector los posibles referenciales para poder rotar el vector 
en 90Grados ya sea en sentido horario o anti-horario
"""

def omegas(vector):
    omega1 = []
    omega2 = []
    
    if vector[2] == 'R': # el vector tiene direccion hacia la derecha
        omega1.append(vector[0])
        omega1.append(vector[1]+1)
        omega1.append('U')      # implica rotacion anti-horario
        
        omega2.append(vector[0])
        omega2.append(vector[1]-1)
        omega2.append('D')  # implica rotacion en sentido horario
    if vector[2] == 'L':    # el vector tiene direccion hacia la izquierda
        omega1.append(vector[0])
        omega1.append(vector[1]+1)
        omega1.append('U')  # implica rotacion anti-horario
        
        omega2.append(vector[0])
        omega2.append(vector[1]-1)
        omega2.append('D')  # implica rotacion en sentido horario
        
    if vector[2] == 'U':    # el vector tiene direccion hacia arriba
        omega1.append(vector[0]+1)
        omega1.append(vector[1])
        omega1.append('R')  # implica rotacion en sentido horario
        
        omega2.append(vector[0]-1)
        omega2.append(vector[1])
        omega2.append('L')  # implica rotacion anti-horario
    if vector[2] == 'D':    # el vector tiene direccion hacia abajo
        omega1.append(vector[0]+1)
        omega1.append(vector[1])
        omega1.append('R') # implica rotacion anti-horario
        
        omega2.append(vector[0]-1)
        omega2.append(vector[1])
        omega2.append('L')  # implica rotacion en sentido horario
    return (omega1, omega2)

"""
La traslacion(p):= sera tal que si p tiene una direccion, la traslcion aplicada
a ese punto respete la direccion del punto. La funcion regresa un punto r 
que es una traslacion de distancia 1 en el la direccion de p
"""
def traslacion(p):
    r = []
    #caso en que la primera operacion realizada fue una T
    if (p[2] == ''):
        aux = randint(0,3)
        if(aux == 0):   # traslacion a la derecha
            r.append(1)
            r.append(0)
            r.append('R')
        if(aux == 1):   # traslacion a la izquierda
            r.append(-1)
            r.append(0)
            r.append('L')
        if(aux == 2): # traslacion a arriba
            r.append(0)
            r.append(1)
            r.append('U')
        if(aux == 3):   # traslacion a abajo
            r.append(0)
            r.append(-1)
            r.append('D')
        return r
    else:
        direccion = p[2]
        if direccion == 'R':
            r.append(p[0] + 1)
            r.append(p[1])
            r.append('R')
            return r
        if direccion == 'L':
            r.append(p[0] - 1)
            r.append(p[1])
            r.append('L')
            return r
        if direccion == 'U':
            r.append(p[0])
            r.append(p[1] + 1)
            r.append('U')
            return r
        if direccion == 'D':
            r.append(p[0])
            r.append(p[1] - 1)
            r.append('D')
            return r

"""
Para cualquier punto p, exiten 2 referenciales(omegas) para poder girar dicho punto
los referenciales son dependiendo de la orientacion que tenga el punto p.
Cada rotacion es con un angulo de 90Grados en sentido horario o anti-horario.
La funcion regresa un punto r que es una rotacion de 90Grados con direccion dependiendo
 del referencial tomado.
"""
def rotacion(p):
    r = []
    #caso en que la primera operacion realizada fue una R
    if (p[2] == ''):
        aux = randint(0,3)
        if(aux == 0):   # obtiene el punto (1,1), y despues se determina la direccion o "angulo" hacia donde se giro
            r.append(1)
            r.append(1)
            aux2 = randint(0,1)
            if(aux2 == 0): # direccion derecha
                r.append('R')
            else:       # direccion arriba
                r.append('U')
        if(aux == 1):   # obtiene el punto (-1,1), y despues se determina la direccion o "angulo" hacia donde se giro
            r.append(-1)
            r.append(1)
            aux2 = randint(0,1)
            if(aux2 == 0): # direccion izquierda
                r.append('L')
            else:       # direccion arriba
                r.append('U')
            
        if(aux == 2): # obtiene el punto (-1,-1), y despues se determina la direccion o "angulo" hacia donde se giro
            r.append(-1)
            r.append(-1)
            aux2 = randint(0,1)
            if(aux2 == 0): # direccion izquierda
                r.append('L')
            else:       # direccion abajo
                r.append('D')

        if(aux == 3):   # obtiene el punto (1,-1), y despues se determina la direccion o "angulo" hacia donde se giro
            r.append(1)
            r.append(-1)
            aux2 = randint(0,1)
            if(aux2 == 0): # direccion derecha
                r.append('R')
            else:       # direccion abajo
                r.append('D')

        return r
    else:
        omgs = omegas(p) # se calculan los omegas para un punto p
        omg_aleatorio = choice(omgs)    # se elige un omega aleatoriamente 
        """ NOTA: en todas las rotaciones, la direccion de las curvas 
            sera la misma orientacion de omg_aleatorio, que indica que 
            la tangente a la recta es correcta"""
        if p[2] == 'R' and omg_aleatorio[2] == 'U':
            r = girar(p,omg_aleatorio,0)    # rotacion en sentido anti-horario con respecto a omg_aleatorio
            r.append('U')
        if p[2] == 'R' and omg_aleatorio[2] == 'D':
            r = girar(p,omg_aleatorio,1)    # rotacion en sentido horario con respecto a omg_aleatorio
            r.append('D')
        if p[2] == 'L' and omg_aleatorio[2] == 'U':
            r = girar(p,omg_aleatorio,1)    # rotacion en sentido horario con respecto a omg_aleatorio
            r.append('U')
        if p[2] == 'L' and omg_aleatorio[2] == 'D':
            r = girar(p,omg_aleatorio,0)    # rotacion en sentido anti-horario con respecto a omg_aleatorio
            r.append('D')
        if p[2] == 'U' and omg_aleatorio[2] == 'L':
            r = girar(p,omg_aleatorio,0)    # rotacion en sentido anti-horario con respecto a omg_aleatorio
            r.append('L')
        if p[2] == 'U' and omg_aleatorio[2] == 'R':
            r = girar(p,omg_aleatorio,1)    # rotacion en sentido horario con respecto a omg_aleatorio
            r.append('R')
        if p[2] == 'D' and omg_aleatorio[2] == 'L':
            r = girar(p,omg_aleatorio,1)    # rotacion en sentido horario con respecto a omg_aleatorio
            r.append('L')
        if p[2] == 'D' and omg_aleatorio[2] == 'R':
            r = girar(p,omg_aleatorio,0)    # rotacion en sentido anti-horario con respecto a omg_aleatorio
            r.append('R')
        return r


def test(x):
    #x = ['T','T','R','R','T','T','R','R']
    inicio = [5,6,'']
    actual = []
    solOp = []
    
    i=0
    while i<8:
        #print ('actual-->',inicio)
        pieza = x[i]
        if pieza == 'T':
            actual = traslacion(inicio)
            solOp.append(actual)
            inicio = actual
            i+=1
        if pieza == 'R':
            actual = rotacion(inicio)
            solOp.append(actual)
            inicio = actual
            i+=1
    vfinal = solOp[7]
    if (vfinal[0] == 0 and vfinal[1] == 0) and vfinal[2] != 'D':
        test(x)
    return (solOp)
    #print('Vector solucion: ', solOp)
    
"""
Esta funcion calcula la permutacion de un arreglo 'vector' 
apartir del indice j hasta el final del arreglo
"""    
def neighbors(vector, j):
    vecinos = []
    v_prima = vector[j:] # vector al que se realiza la permutacion, contiene los elemenos de v desde el indice j hasta el final
    v_complemento = vector[:j]    # contiene los elementos de 'vector' desde el inicio hasta j-1
    permutaciones = list(itertools.permutations(v_prima)) # regresa un conjunto de todas las permutaciones de 'v_prima'
    #print(permutaciones)

    perm_elegida = list(choice(list(permutaciones))) ## esta sera la permutacion elegida del conjunto de permutaciones
    neighbor = v_complemento + perm_elegida  # al final concatenamos el vector que no fue permutado, con el vetor permutado

    #aplico la restriccion de 3 rotaciones seguidas al vecino creado del vector
    #while(restriccion_3rotaciones(neighbor) == 1):
    
    for i in permutaciones:
        
        #print('entro')
        #perm_elegida = list(choice(list(permutaciones))) ## esta sera la permutacion elegida del conjunto de permutaciones
        #neighbor = v_complemento + perm_elegida  # al final concatenamos el vector que no fue permutado, con el vetor permutado
        neighbor = v_complemento + list(i)
    #    vecinos.append(neighbor)
        if (restriccion_3rotaciones(neighbor) != 1):
            vecinos.append(neighbor)
        
    return vecinos

"""
Una restriccion al momento de generar los vecinos o una solucion aleatoria, es que
el vector de T's y R's no debe contener tres R's seguidas. La siguiente funcion 
devuelve un valor 1 si tiene tres R's seguidas y en caso contrario 0
"""
def restriccion_3rotaciones(vector):
    n_rs = [] # este vector contendra cuantas R's estan seguidas
    contador = 0
    """
    Ejemplo: vector = ['T', 'T', 'R', 'R', 'T', 'R', 'T', 'R']
    el vector n_rs =[2,1,1] y si el vector 'n_rs' contiene un 3 entonces
    inidicara que el vector tiene tres R's seguidas
    """
    for i in vector:
        if i == 'R':
            contador +=1
        else:
            n_rs.append(contador)
            contador = 0
    n_rs.append(contador)
    #print (n_rs)
    for j in n_rs:
        if j >= 3:
            return 1
    return 0

"""
La funcion costo determinara la distancia entre
el punto de partida [0,0] y el ultimo vector generado en
la solucion de vectores
"""
def costo(x,y):
    distancia=distance.euclidean(x,y)
    return distancia



def exp_schedule(k=20, lam=0.005, limit=500):
    """One possible schedule function for simulated annealing"""
    return lambda t: (k * math.exp(-lam * t) if t < limit else 0)


def probability(p):
    """Return true with probability p."""
    return p > random.uniform(0.0, 1.0)


def problem_value(vector):
    resultado = []
    aux = test (vector)
    resultado.append(aux)
    delete = []
    X = aux[len(aux)-1]
    delete.append(X[0])
    delete.append(X[1])
    print (delete)
    cost = costo([0,0], delete)
    resultado.append(cost)
    
    return resultado

def conversion(vectores):
    cadena = '['
    for v in vectores:
        cadena += '('
        for vp in v:
            cadena += str(vp)
            cadena += ', '
        cadena += ')'
        cadena += ', '
    cadena += ']'
    return cadena
def indexacion(t):
    j = 0
    if t<=125:
        j = 7
    if t>125 and t<=250:
        j = 5
    if t>250 and t<=375:
        j = 3
    if t>375 and t<=500:
        j = 0
    return j

def recp_datos ():
    f = open("fichero.txt")
    
    lineas = f.readlines()
    for l in lineas:
        print(lineas)
    
    f.close()
def simulated_annealing_full():
    schedule=exp_schedule()
    vec = []
    """ This version returns all the states encountered in reaching 
    the goal state."""
    states = []
    j = 0
    # Abrir fichero.txt donde se gurdaran los resultados
    f = open("fichero.txt", "a")
    
    current = neighbors(['T','T','R','R','T','T','R','R'], j)
    current = choice(current)
    
    for t in range(sys.maxsize):
        print('recocido...')
        states.append(current)
        T = schedule(t)
        #if T == 0:
         #   return states
        # calcular indice j
        j = indexacion(T)
        print (j,T)
        neighbor = neighbors(current, j)
        #if not neighbor:
         #   return current
        next_choice = choice(neighbor)
        
        p1 = problem_value(current)
        p2 = problem_value(next_choice)
        aux1 = p2[1] #costo del estado vecino del actual
        aux2 = p1[1] # costo de la solucion actual
        costos.append(aux2) # guardo todos los costos
        # Escribir en el archivo txt
        aux3 = ' '.join(str(e) for e in current)
        aux3 = aux3 +", "
        aux3= aux3+ str(aux2)
        aux4 = ' '.join(str(e) for e in next_choice)
        aux4 = aux4 + ", "+str(aux1)
        aux4 = aux4 +str(aux1)
        f.write(aux3+', '+conversion(p1[0])+', '+aux4+', '+conversion(p2[0])+'\n')
        print(aux1,aux2)
        if aux2 == 0:
            return (current,p1)
        
        delta_e = aux1 - aux2
        if delta_e > 0 or probability(math.exp(delta_e / T)):
            current = next_choice
        if T == 0:
            return states
    f.close()   
    
#simulated_annealing_full()
