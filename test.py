import torch
import numpy as np

'''
print("Hello, World?")
print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))
'''

from argparse import ArgumentParser



parser1 = ArgumentParser()
parser2 = ArgumentParser(prog="my_example")
parser3 = ArgumentParser(usage="usage")
parser4 = ArgumentParser(description="a simple demo of argparse")
parser5 = ArgumentParser(epilog="see the doc: https://docs.python.org/3/library/argparse.html")

parser1.print_help()
'''
parser = ArgumentParser()
parser.add_argument("pos1", help="positional argument 1")
parser.add_argument("-o", "--optional-arg", help="optional argument", dest="opt", default="default")
args = parser.parse_args()
print("positional arg:", args.pos1)
print("optional arg:", args.opt)


def process_command():
    parser = ArgumentParser()
    parser.add_argument('--foo', help='foo help')
    parser.add_argument('--text', '-t', type=str, required=True, help='Text for program')
    return parser.parse_args()


args = process_command()
print(args.text)
'''
def process_command():
    parser = ArgumentParser()
    g1 = parser.add_argument_group('ahq', '還我西門')
    g1.add_argument('--ahq', action='store_true', default=False, help='Choose ahq')
    g1.add_argument('--text1', '-t1', type=str, default='westdoor will be back', help='note for ahq')
 
    g2 = parser.add_argument_group('jteam', '雷我Fo哥')
    g2.add_argument('--jteam', action='store_true', default=False, help='Choose jteam')
    g2.add_argument('--text2', '-t2', type=str, default='FoFo QQ', help='note for jteam')
 
    return parser.parse_args()
 
if __name__ == '__main__':
    args = process_command()
    if args.ahq:
        print(args.text1)
    if args.jteam:
        print(args.text2)