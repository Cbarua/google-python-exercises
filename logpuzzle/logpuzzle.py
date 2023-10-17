#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

from operator import itemgetter
import os
import re
import sys
import urllib.request
import urllib.error

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  server_url = 'http://' + filename.split('_')[1]
  with open(filename, 'r') as f:
    content = f.read()
    pattern = r'GET (\S+puzzle\S+)'
    puzzle_urls = re.findall(pattern, content)

  def get_last_word(s):
    result = re.search(r"-(\w+)\.", s).group(0)
    return result
  
  puzzle_urls = sorted(list(set(puzzle_urls)), key=get_last_word)
  puzzle_urls = [ server_url + s for s in puzzle_urls ]
  # [print(item) for item in puzzle_urls]
  return puzzle_urls

# read_urls('place_code.google.com')

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  # Create the output directory if it doesn't exist
  os.makedirs(dest_dir, exist_ok=True)

  img_files = []
  if len(os.listdir(dest_dir)) < 20:
    # Download images from the URLs
    for i, url in enumerate(img_urls):
      print('Retrieving .....')
      try:
        # Extract the filename from the URL
        filename = os.path.join(dest_dir, f'img_{i}.jpg')
        
        # Download the image and save it to the specified directory
        urllib.request.urlretrieve(url, filename)
        print(f'Downloaded: {filename}')
        img_files.append(filename.split('\\')[1])
      except urllib.error.URLError:
        print(f'Failed to download: {url}')
  else:
    print('Images are already downloaded')
    for i in len(img_urls):
      img_files.append(f'img_{i}.jpg')
  with open(dest_dir + '/index.html', 'w') as f:
    # Write the HTML content to the file
    f.write('<html>\n')
    f.write('<body>\n')

    # Iterate through image URLs and write <img> tags
    for url in img_files:
      f.write(f'<img src="{url}" alt="Image">\n')

    f.write('</body>\n')
    f.write('</html>\n')
  
  print('HTML file is generated')

# download_images(read_urls('animal_code.google.com'), 'animal')

def main():
  args = sys.argv[1:]

  if not args:
    print('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print('\n'.join(img_urls))

if __name__ == '__main__':
  main()
