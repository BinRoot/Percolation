import numpy as np
import time
import matplotlib.pyplot as plt
plt.ion()

def percolate(state):
    """Generates the next state given the current state
    Arg: 
      state (numpy matrix): the current state of the cellular automata
    Returns:
      numpy matrix: the next state of the automata
    """
    c = np.copy(state)
    for x in range(0, state.shape[0]):
        for y in range(0, state.shape[1]):
            num_ones = 0
            if y > 0 and state[x,y-1] == 1:
                num_ones += 1
            if y < state.shape[1]-1 and state[x,y+1] == 1:
                num_ones += 1
            if x > 0 and state[x-1,y] == 1:
                num_ones += 1
            if x < state.shape[0]-1 and state[x+1,y] == 1:
                num_ones += 1
            if num_ones >= 2:
                c[x,y] = 1
    return c

if __name__ == "__main__":
    # set up board
    m,n = 100,100
    A = np.zeros((m,n))
    A[20,20] = 1
    A[20,22] = 1
    A[22,21] = 1
    A[22,23] = 1
    A[24,23] = 1
    A[24,24] = 1
    A[75,30] = 2
    A[77,30] = 2

    # plot each frame
    plt.figure()
    img_plot = plt.imshow(A, interpolation="nearest", cmap = plt.cm.gray)
    plt.show(block=False)
    wait_time = 0
    while True:
        if wait_time <= 0:
            str = raw_input("Enter number of steps: ")
            if str:
                wait_time = int(str)
        else:
            print(wait_time)
            wait_time -= 1
            A = percolate(A)
            img_plot.set_data(A)
            plt.draw()
            time.sleep(0.01)
