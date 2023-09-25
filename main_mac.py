#!/usr/bin/env python
import os
from glob import glob
from PIL import Image
# this script takes a series of images and creates a GIF.
# saves gif to same directory where JPGs are


def find_all_immediate_sub_dirs(top_dir):
    sub_dirs = []
    try:
        sub_dirs = glob(top_dir + "/**/", recursive = True)
        sub_dirs.pop(0)
    #    sub_dirs = [d.strip("/") for d in glob(top_dir + "*/")]
        for i in sub_dirs:
            print("All subdirectories found to be processed: ", i)
    except:
        print("unable to find subdirectories.  try adding a / at the end of top directory.")
    return sub_dirs


def make_gif(gif_path, gif_name, speed_per_image, pic_extension, gif_sub_dirs: bool):
    all_sub_dirs = []
    frames = []
    path = []
    try:
        path = glob(gif_path + '/' + '*.' + pic_extension)  # get path to JPG files
    except:
        print("unable to detect directory, are you sure it exists?")
    try:
        if gif_sub_dirs:
            all_sub_dirs = find_all_immediate_sub_dirs(gif_path)
            for i in all_sub_dirs:
                stripped_filename = i.split(os.sep)[-2]  # split the filename from the path (-2 gets element in front of 2nd \\ from end)
                print(stripped_filename)
                for paths in path:
                    frames.append(Image.open(paths))
                    frames[0].save(i + '/' + stripped_filename + '.gif', format="GIF", append_images=frames, save_all=True,
                                   duration=speed_per_image,
                                   loop=0)  # save the collection of JPGs as Gif starting with first JPG frame
                print(f"Gif saved as {gif_name}.gif under directory {i}\\")
        else:
            for paths in path:
                frames.append(Image.open(paths))
            frames[0].save(gif_path + '/' + gif_name + '.gif', format="GIF", append_images=frames, save_all=True,
                           duration=speed_per_image,
                           loop=0)  # save the collection of JPGs as Gif starting with first JPG frame
            print(f"Gif saved as {gif_name}.gif under directory {gif_path}\\")
    except:
        print("unable to save GIF!")
    finally:
        again = input("would you like to create another gif? Y/N: ")
        while again == 'y':
            main()
        else:
            exit()


def main():
    print("Welcome to Gif Maker version 0.001.  Created gifs will go into the same folder as the collection of images.")
    input_pic_extension     = input("extension of images to search for in folder (JPG, JPEG, etc): ")
    input_gif_path          = input("Path to collection of images (i.e. c:\\images) or parent folder of "
                                    "sub-directories to iterate through: ")  # Will iterate through all immediate subdirectories
                                                                             # making a GIF in each, (ignoring input_gif_path folder)
                                                                             # AKA batch processing
    input_gif_sub_dirs      = bool(input("include all subdirectories?"))  # will need to change this
    input_gif_name          = input("name of gif to be generated (press enter to use name of folder for batch processing: ")
    input_speed_per_image   = int(input("framerate of gif in ms (100 is default): "))
    make_gif(input_gif_path, input_gif_name, input_speed_per_image, input_pic_extension, input_gif_sub_dirs)


main()


# TODO: regex extension to filter, COMMENT ALL CODE

#def find_all_immediate_sub_dirs(top_dir):
#    return print([x[0] for x in os.walk(top_dir)])
