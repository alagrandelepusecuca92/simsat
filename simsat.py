import argparse
import wallet

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
    def __init__(self):
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="SimSAT Game")
    configure_parser(parser)
    args = parser.parse_args()
