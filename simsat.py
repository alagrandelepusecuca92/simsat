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
    def __init__(self, initial_money, debug=0):
        self.money = initial_money
        self.walletid=0

    def get_money(self):
        return self.money

    def set_money(self, money):
        self.money = money

    def show_me_the_money(self):
        print(self.money)

    def modify_money(self, change):
        self.money += change


class Engine(Wallet, Bank):
    def __init__(self):
        pass
    
    def start(self, wallet=Wallet(), initialtime, endtime):
        currenttime = initialtime
        
        hacer_plazo_fijo = 1
        
        while (currenttime < endtime):
            if (hacer_plazo_fijo == 1):
                wallet = Bank.fixed_term_deposit(wallet, 1000, endtime-currenttime)
            
            wallet
            print ("t=", currenttime, "wallet="wallet.get_money)
            
            currenttime=currenttime+1


class Bank(Wallet):
    def __init__(self, debug=0):
        self.minimun_fixed_term_time = 30 #30*24*60*60
        self.minimun_fixed_term_money = 1000 #30*24*60*60
        self.wallets = [] #[id, status, money] status 1 depositada 2 para retirar
        pass
        
    def fixed_term_deposit(self, walletin = Wallet(), money = 0, time = minimun_fixed_term_time)
        if (time >= minimun_fixed_term_time and money = minimun_fixed_term_money):
            self.wallets.append ([walletin.walletid, 1, money])
            walletin.set_money (walletin.get_money - money);
    
    def check_fixed_term_deposit(self, walletin = Wallet()):
        for wa in self.wallets:
            if (wa[0] == walletin.walletid):
                if (wa[1] == 1):
                    walletin.set_money = walletin.get_money + wa[2]
                    walletin.remove(wa)
   
    def banktime(self,delta_time):
        
        
            
        
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
    unittest.main()
