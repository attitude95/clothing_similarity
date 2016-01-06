import math
import os
from random import sample
import cPickle as pickle

from scipy import spatial
from PIL import Image
import numpy as np

# number of images to compare with input for match
N_IMG = 500

def make_paths_list():
    d = []

    i = 0
    for root, dirs, files in os.walk("clothing_images"):
        for image in files:
            if image.endswith(".jpg"):
                d.append(os.path.join(root, image))
                i += 1
                if i == N_IMG:
                    return d

    raise Error("N_IMG cannot be greater than 1998")


def make_feats(paths):
    #TODO
    pass


def calculate_sim(feats):
    distances = spatial.distance.pdist(np.matrix(feats), 'euclidean')
    m = []
    q = lambda i,j,n: n*(n-1)/2 - (n-i)*(n-i-1)/2 + j - i - 1
    for i in range(N_IMG):
        r = []
        for j in range(N_IMG):
            tup = (distances[q(i,j,N_IMG)], j)
            if i == j:
                tup = (0, j)
            r.append(tup)
        r = sorted(r, key=lambda x: x[0])
        m.append(r)
    return m


def similarity_image(chosen_img, similarity_matrix, paths):
    new_img = Image.new('RGB', (995, 410), "#f8fafc")
    for i in range(10):
        im_num = similarity_matrix[chosen_img][i][1]
        path = paths[im_num]
        img = Image.open(path)
        img.thumbnail((200, 200))
        pos = ((i % 5) * 210, int(math.floor(i / 5.0) * 210))
        new_img.paste(img, pos)
        new_img.save('output/'+ str(N_IMG) + 'if' + str(chosen_img) + '.jpg')
    new_img.show()


def run():
    #TODO
    pass


run()











