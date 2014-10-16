#!/usr/bin/python

import os
import subprocess

FIG_DIR = os.path.dirname(os.path.realpath(__file__))

devnull = open('/dev/null', 'w')

for file in os.listdir(FIG_DIR):
  name, extension = os.path.splitext(file)
  if 'logo' in name:
    print "Ignoring " + file
    continue
  if extension == '.pdf':
    print "Croping " + file
    subprocess.check_call('pdfcrop %s %s' % (file, file), stdout=devnull, shell=True)
  elif extension in ['.jpg', '.png']:
    print "Croping " + file
    subprocess.check_call('convert -trim %s %s' % (file, file), stdout=devnull, shell=True)
