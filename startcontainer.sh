#!/bin/bash

img="pyotr777/jupyter-vtk:latest"
# img="pyotr777/jupyter-foam:u12"
docker run --rm -ti -v $(pwd):/openfoam -p 8888:8888 --name vtk $img /bin/bash

