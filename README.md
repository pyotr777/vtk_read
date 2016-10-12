# OpenFOAM datasets visualisation with VTK and python
 
Convert OpenFOAM data to VTK format with foamToVTK*. Make png images and mp4 movie of scalar and vector data in 3D or 2D projection.

\* foamToVTK is included in OpenFOAM distribution.

### Sample data
Flow between two plane-parallel plates. Top plate is moving with a horizontal velocity V relative to the other and there is 
no pressure gradient.
https://www.scribd.com/document/273227125/OpenFOAM-Tutorial

## Environment 

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
plot_scalar_in_3D_and_2D.ipynb | Compare plotting in 3D and plane projection of scalar data.
Read_VTK.ipynb | Tests reading VTK data and plotting it.
save to flie.ipynb | Save all steps of velocity dynamic into png files with 2D projections.  
velocity_plot_2D.ipynb | Plot velocity vector field in 2D projection.



