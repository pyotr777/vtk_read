#!/bin/bash
# This command uses an old image. Need to install Fenics and plot_vtk_matplotlib.
#docker run --rm -ti -v $(pwd):/openfoam -p 8888:8888 --name vtk pyotr777/jupyter-foam:u12 bash

# New image, not tested yet
docker run --rm -ti -v $(pwd):/openfoam -p 8888:8888 --name vtk pyotr777/jupyter-foam-plotvtk bash
