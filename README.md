# OpenFOAM datasets visualisation with VTK and python
 
Convert OpenFOAM data to VTK format with foamToVTK*. Make png images and mp4 movies of scalar and vector data in 3D or 2D projection.

\* foamToVTK is included in OpenFOAM distribution.

## Sample data
Flow between two plane-parallel plates. Top plate is moving with a horizontal velocity V relative to the other and there is 
no pressure gradient.
https://www.scribd.com/document/273227125/OpenFOAM-Tutorial

## Execution environment 

Run Jupyter notebook in Docker container.

Build Docker image with included Dockerfile.
Sample data is in VTK folder. Mount this folder into container /openfoam directory. Use `./startcontainer.sh` command.

## Requirements

See Dockerfile for required packages and installation steps in Debian (some package names are different in Ubuntu).

# Jupyter notebooks

See notebooks for sample data visualisation code.

## Notebooks

in VTK folder

Notebook | Description
--- | ---
Read_VTK.ipynb | Tests reading VTK data and plotting it.
plot_scalar_in_3D_and_2D.ipynb | Compare plotting in 3D and 2D plane projection of scalar data.
velocity_plot_2D.ipynb | Plot velocity vector field in 2D projection.
save to flie.ipynb | Save velocity dynamics into series of png files with 2D projections.




