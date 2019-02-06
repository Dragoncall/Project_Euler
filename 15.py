from scipy.misc import comb


def number_of_lattice_paths(x,y):
    return int(comb(x+y, x))

if __name__ == '__main__':
    print(number_of_lattice_paths(20,20))