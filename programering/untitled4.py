# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 23:16:53 2021

@author: Sander
"""

class sporsmål:
    def __init__(self, spørsmål, Svar_alternativ, korrekt):
        self.spørsmål = spørsmål
        self.Svar_alternativ = Svar_alternativ
        self.korrekt = korrekt
        
    def __str__(self):
        return f"Spørsmål: {self.spørsmål} Svar alternativ: {self.Svar_alternativ}"
    
    def sjekk_svar(self, Svar):
        
        if self.korrekt== int(Svar): 
            return True
        else:
            return False
            
if __name__ == '__main__':
    #Spørsmål1
    spmtekst = "Hva er 2+2?"        
    Svar_alternativ = ['1', '4', '6']
    fasit = 1 
    s1 = sporsmål(spmtekst, Svar_alternativ, fasit)
    print(s1)
    
    svar_bruker = input("Skriv inn ditt svar: ")
    Bruker_svar = s1.sjekk_svar(svar_bruker)
    print(Bruker_svar)
    
    #Spørsmål2
    spmtekst2 = "Hvilken farge er en bannan?"
    Svar_alternativ2 = ["gul", "rød", "blå"]
    fasit2 = 0
    s2 = sporsmål(spmtekst2, Svar_alternativ2, fasit2)
    print(s2)
    
    svar_bruker2 = input("Skriv inn ditt svar (0 = gul, 1 = rød, 2 = blå: ")
    Bruker_svar2 = s2.sjekk_svar(svar_bruker2)
    print(Bruker_svar2)