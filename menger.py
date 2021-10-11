import matplotlib.pyplot as plt
import numpy as np

def generate_menger_array(iterations, base_x, base_y, base_z, n, voxels_array, x, y, z):
    if iterations == 0:
        return
    unit = voxels_array.shape[0] * 1.0 / 3**(n + 1 - iterations)
    tunnel1 = (x < base_x + unit * 2) & (x >= base_x + unit) & (y < base_y + unit * 2) & (y >= base_y + unit) & (z >= base_z) & (z < base_z + 3 * unit)
    tunnel2 = (z < base_z + unit * 2) & (z >= base_z + unit) & (y < base_y + unit * 2) & (y >= base_y + unit) & (x >= base_x) & (x < base_x + 3 * unit)
    tunnel3 = (x < base_x + unit * 2) & (x >= base_x + unit) & (z < base_z + unit * 2) & (z >= base_z + unit) & (y >= base_y) & (y < base_y + 3 * unit)
    voxels_array &= ~(tunnel1 | tunnel2 | tunnel3)

    for new_base_x in range(3):
        for new_base_y in range(3):
            for new_base_z in range(3):
                if not((new_base_x == 1 and new_base_y == 1) or (new_base_x == 1 and new_base_z == 1) or (new_base_y == 1 and new_base_z == 1)):
                    generate_menger_array(iterations - 1, base_x + new_base_x * unit, base_y + new_base_y * unit, base_z + new_base_z * unit, n, voxels_array, x, y, z)

def generate_graph(iterations):
    n = iterations
    dimen = (3**n, 3**n, 3**n)
    x, y, z = np.indices(dimen)
    voxels_array = np.ones(dimen, dtype=np.bool)

    generate_menger_array(n, 0, 0, 0, n, voxels_array, x, y, z)

    ax = plt.figure().add_subplot(projection='3d')
    ax.voxels(voxels_array)
    plt.show()

if __name__ == "__main__":
    # change this line to generate Menger Sponge of a different iteration
    iterations = 2
    generate_graph(iterations)