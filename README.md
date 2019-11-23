# 親子天下故事有聲書匯出工具

This tool helps you export the audiobooks you've purchased on [親子天下故事有聲書 APP](https://www.parenting.com.tw/event/storyapp). I like the quality content on that platform, but the stability of the Android app could be better. Having kids whining about the crashing app while driving on the highway is not fun! I hacked a simple script to export them so that I can enjoy the content on other audio players.

## Prerequisites

This script only works on rooted Android devices with USB debugging enabled. For most end-users, the easiest way might be installing the app again in an Android Emulator and downloading your purchased audiobooks there.

The scripts are targeting Linux. I believe it could work on Mac or even Cygwin for other platforms with reasonable effort, so pull requests are welcomed. :)

The script depends on other packages, so install them before running it.

```
sudo apt install android-tools-adb libxml2-utils python3 eyed3
```

## Usage

Run the script this way:
```
cd ~/Downloads/parenting/
./download.sh
```

Afterwards, the extracted MP3 files should show up in the current folder, with ID3 tags containing the correct title, album, artist, and track numbers. You can later import them into most audio players.

## License

This project is licensed under the MIT License.
