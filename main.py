#!/usr/bin/python3

import argparse
import sys
import cv2
import os

parser = argparse.ArgumentParser(description='Process video extract frames.')
parser.add_argument('-v', '--video_file', help='Video to extract frames from.', required=True)
parser.add_argument('-d', '--dest_dir', help='Destination directory to store images.', default='Imgs')
parser.add_argument('-e', '--ext', help='Image extention to store in format.', default='png')
parser.add_argument('-n', '--num_img', help='Number of images to extract.', default='100')
args = parser.parse_args()

video = cv2.VideoCapture(args.video_file)
fps = video.get(cv2.CAP_PROP_FPS)
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
num_imgs = int(args.num_img)

if num_imgs > total_frames:
    print("Requested Number of Images are Higher Than Total Frams in Video.")
    sys.exit()

elif num_imgs > (total_frames / fps):
    print("Warning: Requested Number of Images are Higher Than 1 Image Per Second")

if not os.path.exists(args.dest_dir):
    os.makedirs(args.dest_dir)

image_per_frames = total_frames // num_imgs

img_count = 1
n = 1

for i in range(total_frames):
    ret, frame = video.read()
    if n >= image_per_frames:
        img_name = 'image_' + str(img_count) + '.' + args.ext
        path = os.path.join(args.dest_dir, img_name)
        cv2.imwrite(path, frame)
        img_count += 1
        n = 0
    n += 1
