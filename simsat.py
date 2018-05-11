import argparse
import time

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

def configure_parser(parser):
    parser.add_argument("-t", "--run_time", type=int, default=60,
                        help="Run time in seconds (default: %(default)d)")
    parser.add_argument("-m", "--initial_money", type=int, default=1000,
                        help="Initial money (default: %(default)d)")
    parser.add_argument("-r", "--decrease_rate",  type=int, default=1,
                        help="Rate at which money decreases, in percentage (default: %(default)d)")

class Wallet():
    def __init__(self, initial_money, debug=0):
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
    def __init__(self, initial_money, decrease_rate):
        self.wallet = Wallet(initial_money)
        self.decrease_rate = decrease_rate

    def run(self, run_time):
        print('Watch how inflation kills your savings over time:')
        end_time = time.time() + run_time
        while time.time() < end_time:
            print('Current money: {}'.format(self.wallet.get_money()))
            time.sleep(1)
            self.wallet.set_money((1-self.decrease_rate/100)*self.wallet.money)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This script runs a wallet engine for a given time, with a given ' +\
                                                'initial money.')
    configure_parser(parser)
    args = parser.parse_args()
    
    engine = Engine(args.initial_money, args.decrease_rate)
    engine.run(args.run_time)
