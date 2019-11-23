#!/bin/bash

adb root
adb pull /data/data/com.parenting.story/files/ParentingMedia
adb pull /data/data/com.parenting.story/shared_prefs/ParentingLogin.xml
xmllint ParentingLogin.xml --xpath '/map/string[@name="OfflineAlbumData"]/text()' > offline.json
cat offline.json | ./extract.py
