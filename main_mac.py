#!/usr/bin/env python
import glob

from PIL import Image


# saves gif to same directory where JPGs are

def make_gif(gif_path, gif_name, speed_per_image, pic_extension):
    try:
        path = glob.glob(gif_path + '/' + '*.' + pic_extension)  # get path to JPG files
#        print(f"length of path: {len(path)}")
    except:
        print("unable to detect directory, are you sure it exists?")
    try:
        frames = [Image.open(path) for path in path]  # store each JPG in frames array
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
    input_pic_extension = input("extension of images to search for in folder (JPG, JPEG, etc): ")
    input_gif_path = input("Path to collection of images (i.e. c:\\images): ")
    input_gif_name = input("name of gif to be generated: ")
    input_speed_per_image = int(input("framerate of gif in ms (100 is default): "))
    make_gif(input_gif_path, input_gif_name, input_speed_per_image, input_pic_extension)



main()


# TODO: regex extension to filter .