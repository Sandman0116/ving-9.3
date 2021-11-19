# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 23:05:00 2021

@author: Sander
"""

# Klasse for flervalgsspørsmål
class Multichoice:
    def __init__(self, question, correct, options):
        self.question = question
        self.options = options
        self.correct = int(correct)
        

    def __str__(self):
        result = self.question + "\nAnswer options:\n"
        for index, verdi in enumerate(self.options):
            result += f"{index}: {verdi}\n"
        return result
    
    def check_response(self, response):
        if int(response) == self.correct:
            print("Correct!")
        else:
            print("No!")
            
    def correct_response_text(self):
        correct_answer = self.correct
        return f"Correct answer is {self.options[correct_answer]}"


if __name__ == "__main__":
    quiz = list()
    spiller1 = [0, 0]
    spiller2 = [0, 0]
    
    with open("sporsmal.txt", "r", encoding="UTF8") as fila:
        for linje in fila:
            verdier = linje.split(":")
            alternativer = verdier[2].strip("[").strip("]").split(",")
            sporsmal = Multichoice(verdier[0], verdier[1], alternativer)
            quiz.append(sporsmal)
    
    for i in quiz:
        print(i)
        spiller1[0] = int(input("P1 Answer (Number preceding the option):"))
        spiller2[0] = int(input("P2 Answer (Number preceding the option):"))
        print("\n",i.correct_response_text(),"\n")
        if spiller1[0] == i.correct:
            print("P1: Correct")
            spiller1[1] += 1
        else:
            print("P1: Wrong")
        if spiller2[0] == i.correct:
            print("P2: Correct")
            spiller2[1] += 1
        else:
            print("P2: Wrong")
    print(f"\nGame over! Final scores:\nP1: {spiller1[1]}\nP2: {spiller2[1]}")
        
    
    
