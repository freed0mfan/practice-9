parameters = input('[N_d_R]: ')
N, d, R = int(parameters.split(' ')[0]), int(parameters.split(' ')[1]), int(parameters.split(' ')[2])
L = 2 * (R + d) * N - 2 * d * (N - 1)
print('L =', L)
