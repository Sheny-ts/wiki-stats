#!/usr/bin/python3

import os
import sys
import math

import array

import statistics

import codecs

from matplotlib import rc
rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt


class WikiGraph:

    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)

        with codecs.open(filename, 'r', 'utf-8') as f:
            (n, _nlinks) = map(int, f.readline().split())

            self._titles = []
            self._sizes = array.array('L', [0]*n)
            self._links = array.array('L', [0]*_nlinks)
            self._redirect = array.array('B', [0]*n)
            self._offset = array.array('L', [0]*(n+1))

            for i in range(n-1):
                name = f.readline().rstrip()
                size, flag, n0 = map(int, f.readline().rstrip().split())
                self._titles.append(name)
                self._sizes[i] = size
                self._redirect[i] = flag
                self._offset[i] = self._offset[i-1] + n0
                for j in range(n0):
                    k = int(f.readline().rstrip())
                    self._links[i+j] = k

        print('Graph downloaded')

    def get_number_of_links_from(self, _id):
        return self._offset[_id + 1] - self._offset[_id]

    def get_links_from(self, _id):
        return self._links[_offset[_id]:self._offset[_id + 1]]

    def get_id(self, title):
        return self._titles.index(title)

    def get_number_of_pages(self):
        return self._n

    def is_redirect(self, _id):
        return self._redirect[_id]

    def get_title(self, _id):
        return self._titles[_id]

    def get_page_size(self, _id):
        return self._sizes[_id]


def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Использование: wiki_stats.py <файл с графом статей>')
        sys.exit(-1)

    if os.path.isfile(sys.argv[1]):
        wg = WikiGraph()
        wg.load_from_file('wiki_small.txt')
    else:
        print('Файл с графом не найден')
        sys.exit(-1)

    # TODO: статистика и гистограммы

