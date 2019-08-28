#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 13:33:20 2019

@author: vitor
"""
import math

def fx(x): #função que deseja achar a raiz
    
    return x**3-9*x+5
#%%
def gx(x): #função usada para o método do ponto fixo
        return (x**3+5)/9
#%%
def bisec(a,b,erro):
    
    print('Método do Ponto Fixo \n Precisão: %.4f \n| i| g(x) | f(x) | x | | sinal | ' %erro)
    n = 1
    x_medio = (a+b)/2
    while abs(fx(x_medio))>erro:
        
        
        if fx(x_medio)*fx(a) < 0: # b recebe x_medio
            
            sinal = '-'
            print('| %d | %.3f | %.3f | %.3f | %s |' %(n,a,b,x_medio, sinal))
            b = x_medio
        if fx(x_medio)*fx(a) > 0: # a recebe x_medio
            
            sinal = '+'
            print('| %d | %.3f | %.3f | %.3f | %s |' %(n,a,b,x_medio, sinal))
            a = x_medio
        x_medio = (a+b)/2 #atualiza x médio
        n+=1 #atualiza º de interações
    print('| %d | %.3f | %.3f | %.3f | %s |' %(n,a,b,x_medio, sinal))
#%%
def falsapos(a,b,erro): # implementação do método da falsa posição
    """ Esta função difere do método da bisecção 
    apenas no fato de o x_médio ser calculado como 
    uma média ponderada. x_medio = (af(b)-bf(a))/(f(b)-f(a))"""
    
    print('Método da Falsa Posição \n Precisão: %.4f \n| i| g(x) | f(x) | x | | sinal | ' %erro)
    n = 1
    x_medio = (a*fx(b)-b*fx(a))/(fx(b)-fx(a))
    
    while abs(fx(x_medio))> erro:
        
        if fx(x_medio)*fx(a) < 0: # b recebe x_medio
            
            sinal = '-'
            print('| %d | %.3f | %.3f | %.3f | %s |' %(n,a,b,x_medio, sinal))
            b = x_medio
        if fx(x_medio)*fx(a) > 0: # a recebe x_medio
            
            sinal = '+'
            print('| %d | %.3f | %.3f | %.3f | %s |' %(n,a,b,x_medio, sinal))
            a = x_medio
        x_medio = (a*fx(b)-b*fx(a))/(fx(b)-fx(a)) #atualiza x médio
        n+=1 #atualiza º de interações
    print('| %d | %.3f | %.3f | %.3f | %s |' %(n,a,b,x_medio, sinal))
    

#%%
def ptofix(chute,erro): # implementação do método do ponto fixo, recebe um chute inicial para o valor da raiz e o erro
    
    n = 0
    x = chute 
    print('Método do Ponto Fixo \n Precisão: %.4f \n| i| g(x) | f(x) | x | | sinal | ' %erro)

    if abs(fx(x)) < erro: # verifica se o chute já não é o próprio valor da raiz
            return print(gx(x))
    else:
        while abs(fx(x)) > erro: #enquanto |f(x)| for maior que o erro
        
            print('| %d | %.3f | %.3f | %.3f | n/a |' %(n,gx(x),fx(x),x))
            x = gx(x) # recebe g(x)
            n+=1 #atualiza nº de interações
        print('| %d | %.3f | %.3f | %.3f | n/a |' %(n,gx(x),fx(x),x))
        
#%%
#def secante ():
    
#%%

def main():
    bisec(0.5,1,10E-3)
    print('\n')
    falsapos(0.5,1,10e-3)
    print('\n')
    ptofix(0.75,10E-3)

main()