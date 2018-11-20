import sys, time

BAILOUT = 16
MAX_ITERATIONS = 1000

class example(object):

    def __init__(self):

        print('Running...')
        value = self.multiplier(2.7, 3.5)
        self.bug(value)
        self.file_bug('example.py')

    def multiplier(self, x, y):
        result = x * y
        return result

    def bug(self, value):

        for number in value:
            print(number)

        for nuber in value:
            print(number)

    def file_bug(self, fname):
        # with open(fname, 'r') as fp:
        #     lines = fp.readlines()
        fp = open(fname, 'r')
        lines = fp.readlines()
        fp.close()
        print('file read done')

t = time.time()
example()
print('\nPython Elapsed %.02f' % (time.time() - t))