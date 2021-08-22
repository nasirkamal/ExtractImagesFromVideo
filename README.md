### 1) Install Python3:
[Install Python](https://www.python.org/downloads/)
### 2) Install Dependencies:

`pip3 install -r requirements.txt`


### 3) Run Script:

`./main.py -v video.mp4 -n 200`

### 4) For Help:

`./main.py -h`
```
usage: main.py [-h] -v VIDEO_FILE [-d DEST_DIR] [-e EXT] [-n NUM_IMG]

Process video extract frames.

optional arguments:
  -h, --help            show this help message and exit
  -v VIDEO_FILE, --video_file VIDEO_FILE
                        Video to extract frames from.
  -d DEST_DIR, --dest_dir DEST_DIR
                        Destination directory to store images.
  -e EXT, --ext EXT     Image extention to store in format.
  -n NUM_IMG, --num_img NUM_IMG
                        Number of images to extract.
```
