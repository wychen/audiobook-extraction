#!/usr/bin/python3

import html
import os
import sys
import json
import shutil
import eyed3

data = json.loads(sys.stdin.read())['result']

for album in data:
  album_name = html.unescape(album['album_name'])
  if album_name == u'月月聽':
    print('Skip %s' % album_name)
    continue
  print(album_name)
  stories = album['story']
  track_num = 0
  for story in stories:
    track_num += 1
    story_name = html.unescape(story['story_name'])
    local_filename = 'ParentingMedia/%s.mp3' % story['story_id']
    if not os.path.exists(local_filename):
      print('%s %s is not downloaded yet' % (album_name, story_name))
      continue

    filename = '%s/%s.mp3' % (album_name, story_name)
    os.makedirs(album_name, exist_ok=True)
    shutil.copy(local_filename, filename)
    print('Processing %s' % filename)

    mp3 = eyed3.load(filename)
    mp3.initTag()
    tag = mp3.tag
    tag.title = story_name
    tag.album = album_name
    tag.artist = u'親子天下'
    tag.track_num = (track_num, len(stories))
    tag.save()
