#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
# returns a list of the absolute paths of the special files in the given directory
def get_special_paths(dir):
  filenames = os.listdir(dir)
  # print(filenames)
  pattern = r'__\w+__'
  special_files = [s for s in filenames if re.search(pattern, s)]
  special_file_paths = []
  for path in special_files:
    special_file_paths.append(os.path.abspath(os.path.join(dir, path)))
  return special_file_paths

# given a list of paths, copies those files into the given directory
def copy_to(paths, dir):
  if not dir[-1] == '\\': dir = dir + '\\'
  print(dir)
  if not os.path.exists(dir):
    os.mkdir(dir)
  
  for path in paths:
    # print(f'Src: {path} => Des: {dir}')
    print(shutil.copy(path, dir))
  return

# given a list of paths, zip those files up into the given zipfile
def zip_to(paths, zippath):
  try:
    # Construct the command with proper quotes
    cmd = f'"C:\\Program Files\\7-Zip\\7z.exe" a "{zippath}" {" ".join(paths)}'
    print(f'Command I\'m going to do: {cmd}')
    
    # Run the 7-Zip command
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

    print("Compression successful.")
    print(result.stdout)

  except subprocess.CalledProcessError as e:
    print(f"Compression failed. Return code: {e.returncode}")
    print("Standard Output:")
    print(e.stdout)
    print("Standard Error:")
    print(e.stderr)

  except FileNotFoundError:
    print("7-Zip executable not found. Please ensure it's installed in the specified path.")


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print('usage: [--todir dir][--tozip zipfile] dir [dir ...]')
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    copy_to(get_special_paths(args[2]), todir)
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    zip_to(get_special_paths(args[2]), tozip)
    del args[0:2]

  if not args: # A zero length array evaluates to "False".
    print('error: must specify one or more dirs')
    sys.exit(1)
  # else:
    # print(get_special_paths(args[0]))

  # +++your code here+++
  # Call your functions

if __name__ == '__main__':
  main()
