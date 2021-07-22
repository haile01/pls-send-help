#!/usr/bin/env python3

import sys
import os
from PIL import ImageGrab
import subprocess

def is_jpg (content):
  return content[:2] == b'\xff\xd8'

def is_png (content):
  return content[:4] == b'\x89\x50\x4e\x47'

def invalid_file ():
  print('Oops, it seems like the file is not image :(')

def get_files ():
  path = './acv/'
  if not os.path.exists(path):
    os.makedirs(path)
  files = ["'" + os.path.join(path, f)[2:] + "'" for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
  return files

def add_image (path):
  file_content = open(path, 'rb').read()
  if not is_jpg(file_content) and not is_png(file_content):
    invalid_file()
    return
  
  file_type = path.split('.')[-1]
  cnt_file = len(get_files())
  open('./acv/' + str(cnt_file) + '.' + file_type, 'wb').write(file_content)
  
  print('Yay, one more achievement added :3')

def add_image_clipboard ():
  image = ImageGrab.grabclipboard()
  if image == None:
    print('Oops, can\'t find any image in clipboard')
    return
  
  if type(image) == list:
    add_image(image[0])
    return

  cnt_file = len(get_files())
  image.save('./acv/' + str(cnt_file) + '.png', 'PNG')
  
  print('Yay, one more achievement added :3')

def send_help ():
  # Edit template file, too lazy to run server and render_template :(
  # I'm sad duh
  template = open('help.html', 'r').read()
  begin_acv = template.find('// BEGIN ACV') + len('// BEGIN ACV')
  end_acv = template.find('// END ACV')

  files = ',\n'.join(get_files())
  template = template[:begin_acv] + '\n' + files + '\n' + template[end_acv:]
  open('help.html', 'w').write(template)

if len(sys.argv) > 1:
  if sys.argv[1] == '-a':
    # Add image by path
    path = sys.argv[2]
    add_image(path)
  elif sys.argv[1] == '-ac':
    add_image_clipboard()
else:
  send_help()
  subprocess.Popen('explorer ' + os.path.abspath('./help.html'))