import unittest
import argparse

sate = '''
                }--O--{
                  [^]
                 /ooo\\
 ______________:/o   o\:______________
|=|=|=|=|=|=|:A|":|||:"|A:|=|=|=|=|=|=|
^""""""""""""""!::{o}::!""""""""""""""^
                \     /
                 \.../
      ____       "---"       ____
     |\/\/|=======|*|=======|\/\/|
     :-----       /-\       -----:
                 /ooo\\
                #|ooo|#
                 \___/'''


class Wallet():
    def __init__(self, initial_money=0, debug=0):
        self.money = initial_money

    def get_money(self):
        return self.money

    def set_money(self, money):
        self.money = money

    def show_me_the_money(self):
        print(self.money)

    def modify_money(self, change):
        self.money += change


class Engine():
    def __init__(self, initial_time=0, initial_money=0):
        self.wallet = Wallet(initial_money)
        self.time = initial_time
        
    def run(self, initialtime=0, endtime=0):
        currenttime = initialtime
        
        while (currenttime < endtime):
            print ("t=" + str(currenttime) + " wallet=" + str(self.wallet.get_money()))
            currenttime=currenttime+1
            
    def update (self, deltatime = 0):
        self.time = self.time + deltatime
        #actualizo wallet
        
    def status (self):
        return [self.time, self.wallet.get_money()]

if __name__ == '__main__':
    buscadordeparametros = argparse.ArgumentParser()
    buscadordeparametros.add_argument("tini", type=int, help="Tiempo inicial")
    buscadordeparametros.add_argument("tfin", type=int, help="Tiempo final")
    buscadordeparametros.add_argument("pini", type=int, help="Plata inicial")
    args = buscadordeparametros.parse_args()
    
    eng = Engine(args.tini, args.pini)
    print(eng.status())
    
    while (eng.status()[0] < args.tfin):
        eng.update(1)
        print(eng.status())
        
    print ("fin")
