import argparse
import finance

def configure_parser(parser):
    parser.add_argument("-t", "--time",  type=int, default=10,   help="Time in seconds (default: %(default)d)")
    parser.add_argument("-m", "--money", type=int, default=1000, help="Money in bitcoins (default: %(default)d)")


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

class Engine():
    def __init__(self, money, time):
        self.wallet = finance.Wallet(money)
        self.time_money_conv = 10

    def transfer_money (self, time):
        self.wallet.modify_money(time*self.time_money_conv)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="SimSAT Game")
    configure_parser(parser)
    args = parser.parse_args()
    print('Guita Inicial:  {}'.format(args.money))
    print('Tiempo Total: {}'.format(args.time))

    engine = Engine(args.money, args.time)
    engine.transfer_money(args.time)
    print('Guita al final del juego: %d' % engine.wallet.get_money())
