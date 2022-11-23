from src.mesher import create_mesh

import dolfin

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.tri as tri


mesh=create_mesh(1,2,20)

n = mesh.num_vertices()
d = mesh.geometry().dim()

# Create the triangulation
mesh_coordinates = mesh.coordinates().reshape((n, d))
triangles = np.asarray([cell.entities(0) for cell in dolfin.cells(mesh)])
triangulation = tri.Triangulation(mesh_coordinates[:, 0],
                                  mesh_coordinates[:, 1],
                                  triangles)

# Plot the mesh
plt.figure()
plt.triplot(triangulation)
plt.savefig('../outputs/mesh.png')

dolfin.plot(mesh)