""" Test.py

    Usage:
        Test.py -h
        Test.py <required> [-f | -g | -o ]
        Test.py <repeating>...
    Options:
        -h,--help       : show this help message
        required        : example of a required argument
        repeating       : example of repeating arguments
        -f,--flag       : example flag #1
        -g,--greatflag  : example of flag #2
        -o,--otherflag  : example of flag #3
"""
from docopt import docopt
import sys

def main(docopt_args,args):
    print('This is test')
    if docopt_args["<required>"]:
        print("You have used the required argument: " + docopt_args["<required>"])

        # Get flags used
        if docopt_args["--flag"]:
            print("   with --flag\n")
        elif docopt_args["--greatflag"]:
            print("   with --greatflag\n")
        elif docopt_args["--otherflag"]:
            print("   with --otherflag\n")
        else:
            print("   with no flags.\n")
        # User passed 1 or more repeating arguments
    elif docopt_args["<repeating>"]:
        print("You have used the repeating args:")
        print('   ' + '\n   '.join(docopt_args["<repeating>"]) + '\n')


args = docopt(__doc__, version='0.1.0 alpha')
main(args,sys.argv)

