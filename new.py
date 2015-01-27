#!/usr/bin/python

import os
import argparse
import subprocess

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
TEMPLATES = [t for t in os.listdir(ROOT_DIR) if os.path.isdir(os.path.join(ROOT_DIR, t)) and t not in ['common', '.git']]

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--dest', default=os.getcwd(), help="Destination directory.")
parser.add_argument('template', choices=TEMPLATES, help="Template to create.")


args = parser.parse_args()

try:
  os.makedirs(os.path.join(args.dest, 'figs'))
except:
  pass

for dir in ['common', args.template]:
  for file in os.listdir(os.path.join(ROOT_DIR, dir)):
    subprocess.check_call('cp -riv %s %s' % (os.path.join(ROOT_DIR, dir, file), os.path.join(args.dest)), shell=True)
