#!/usr/bin/python

import os
import argparse
import subprocess

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
TEMPLATES = [t for t in os.listdir(ROOT_DIR)
             if os.path.isdir(os.path.join(ROOT_DIR, t)) and
             t not in ['common', '.git']]


def argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('template', choices=TEMPLATES,
                        help="Template to create.")
    parser.add_argument('-d', '--dest', default=os.getcwd(),
                        help="Destination directory.")
    return parser


def main():
    args = argparser.parse_args()

    try:
        os.makedirs(args.dest)
    except:
        pass

    for dir in ['common', args.template]:
        subprocess.check_call('cp -riv %s/* %s/' %
                              (os.path.join(ROOT_DIR, dir),
                               os.path.join(args.dest)), shell=True)


if __name__ == '__main__':
    main()
