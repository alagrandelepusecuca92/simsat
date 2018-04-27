import unittest


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
    def __init__(self):
        self.wallet = Wallet(100)
        self.time = 0
        
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


class TestWallet(unittest.TestCase):
    def setUp(self):
        self.wallet = Wallet(100)

    def test_default_money(self):
        self.assertEqual(100, self.wallet.money)

    def test_increase_money(self):
        self.wallet.modify_money(10)
        self.assertEqual(110, self.wallet.money)

    def test_decrease_money(self):
        self.wallet.modify_money(-30)
        self.assertEqual(70, self.wallet.money)

    def test_getter_money(self):
        self.assertEqual(100, self.wallet.get_money())

    def test_setter_money(self):
        self.wallet.set_money(10)
        self.assertEqual(10, self.wallet.get_money())


if __name__ == '__main__':
    eng = Engine()
    print ("estado actual")
    print(eng.status())
    print ("actualizo con 10 deltas")
    eng.update(10)
    print ("estado despues")
    print(eng.status())
