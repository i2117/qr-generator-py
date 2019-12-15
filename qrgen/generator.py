import os
from PIL import Image, ImageDraw
import random

dict

class Generator:

    def __init__(self, fragment_size, fragment_count, common_name, delimeter, start_index, end_index):
        self.__fragment_size = int(fragment_size)
        self.__fragment_count = int(fragment_count)
        self.__common_name = common_name
        self.__delimeter = delimeter
        self.__start_index = int(start_index)
        self.__end_index = int(end_index)

    def __init__2(self, params={
                 'fragment_size': 5,
                 'fragment_count': 20,
                 'common_name': 'mark',
                 'delimeter': '_',
                 'start_index': 0,
                 'end_index': 3
    }):
        self.__fragment_size = int(params['fragment_size'])
        self.__fragment_count = int(params['fragment_count'])
        self.__common_name = params['common_name']
        self.__delimeter = params['delimeter']
        self.__start_index = int(params['start_index'])
        self.__end_index = int(params['end_index'])
        #self.__folder_path = os.path.join(self.common_path, common_name)

    common_path = 'temporary_marks'

    def __random_bool(self):
        return bool(random.getrandbits(1))

    def __mark(self):
        size_in_pixels = self.__fragment_size * self.__fragment_count
        img = Image.new('RGB', (size_in_pixels, size_in_pixels), color='white')
        draw = ImageDraw.Draw(img)
        for y in range(self.__fragment_count):
            y_0 = y * self.__fragment_size
            y_1 = (y + 1) * self.__fragment_size
            for x in range(self.__fragment_count):
                if self.__random_bool():
                    x_0 = x * self.__fragment_size
                    x_1 = (x + 1) * self.__fragment_size
                    xy = [(x_0, y_0), (x_1, y_1)]
                    #print(x, y)
                    #ImageDraw.floodfill(img, (x_0, x_1), value=(1,1,1))
                    draw.rectangle(xy, fill='black')
        return img

    def generate_to(self, folder_name):
        folder_path = os.path.join(self.common_path, folder_name)
        if not os.path.isdir(folder_path):
            os.makedirs(folder_path)
        for i in range(self.__start_index, self.__end_index):
            full_path = os.path.join(
                folder_path, self.__common_name + self.__delimeter + str(i) + '.png')
            self.__mark().save(full_path)