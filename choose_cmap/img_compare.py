import random
import copy
from PIL import Image
import matplotlib.pyplot as plt

INSTRUCTIONS="""INSTRUCTIONS
============

You will be shown two images. Image A is on the left and Image B is on the right.
When you see the images, pick which one you prefer, A or B.
Once you have chosen, close the window and enter your response, A or B at the prompt.
"""


def show_images(A, B):
    """
    Compare open two images (A and B) as subplots with matplotlib.
    The images should be PIL.Image instances.
    """

    fig = plt.figure("Pick the better image. Remember your choice (A or B).")
    
    ax = fig.add_subplot(1, 2, 1)
    ax.imshow(A)
    ax.set_title('Image A')
    plt.axis("off")
 
    ax = fig.add_subplot(1, 2, 2)
    ax.imshow(B)
    ax.set_title('Image B')
    plt.axis("off")

    plt.show()


def prompt(valid_responses):
    """
    Prompt the user for the better image with a loop.

    valid_responses should be a list of all caps strings.
    """
    response = input('Which was the better image? (A or B) ').upper()
    attempts = 1
    while response not in valid_responses:
        if attempts == 3:
            print(INSTRUCTIONS)
            input('Press any key to continue.')
        if attempts > 10:
            print('10 attempts taken. Exiting')
            exit(0)
        response = input('Wrong. A or B? ').upper()
    return response 


def main(images):
    # open the images as PIL.Image instances
    images_dict = {fname: Image.open(fname) for fname in images}
    images = list(images_dict.values())

    print(INSTRUCTIONS)
    input('Press any key to continue.')

    # loop
    while len(images) > 1:
        # shuffle images
        random.shuffle(images)
        new_images = []
        # we'll be lazy and if there is an odd one then the last image gets a bye.
        if len(images) % 2 == 1:
            new_images.append(images.pop())
        for i in range(0, len(images), 2):
            iA = i
            iB = i+1
            print('Showing next image. Open the Matplotlib window.')
            show_images(images[iA], images[iB])
            responses = {'A': [iA], 'B': [iB], 'SKIP': [iA, iB], 'EXIT': 'exit'}
            response = responses[prompt(list(responses.keys()))]
            if response == 'exit':
                print('Remaining image names were {}'.format([list(images_dict.keys())[list(images_dict.values()).index(images[i])] for i in range(len(images))]))
                print('Exiting')
                exit(0)
            new_images.extend([images[i] for i in response])
        # set the images to the new images we constructed
        images = new_images
    # return the name of the winning image
    print('The winning image was: {}'.format((list(images_dict.keys())[list(images_dict.values()).index(images[0])])))

if __name__ == '__main__':
    # TODO: take in image files as args
    # image files
    images = ["contourf-lin-50-more_pts-OrRd.png", "contourf-lin-50-more_pts-Oranges.png", "contourf-lin-50-more_pts-RdBu_r.png", "contourf-lin-50-more_pts-Reds.png", "contourf-lin-50-more_pts-Wistia.png", "contourf-lin-50-more_pts-YlOrRd.png", "contourf-lin-50-more_pts-autumn_r.png", "contourf-lin-50-more_pts-coolwarm.png", "contourf-lin-50-more_pts-gnuplot.png", "contourf-lin-50-more_pts-gnuplot2.png", "contourf-lin-50-more_pts-inferno.png", "contourf-lin-50-more_pts-jet.png", "contourf-lin-50-more_pts-nipy_spectral.png", "contourf-lin-50-more_pts-plasma.png", "contourf-lin-50-more_pts-rainbow.png", "contourf-lin-50-more_pts-viridis.png"]

    main(images)

