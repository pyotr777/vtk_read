# OpenFOAM datasets visualisation with matlplotlib and python
 
Convert OpenFOAM data to VTK format with foamToVTK*. Create images and movies of 2D and 3D plots of scalar and vector data using python and matplotlib.

Can be used in automated workflows with no user interaction.

\* <span style="font-size:9pt;color:#777;">foamToVTK is included in OpenFOAM distribution.</span>

## Sample data
Flow between two plane-parallel plates. Top plate is moving with a horizontal velocity V relative to the other and there is 
no pressure gradient.
https://www.scribd.com/document/273227125/OpenFOAM-Tutorial

### Static images compared to Paraview

##### Pressure distribution in Paraview
![Paraview pressure](sample_images/paraview_p1.png "Paraview pressure ")

##### And in matplotlib: side panel surfaces in 3D and in XY plane (Z=0)
![Matplotlib pressure](sample_images/vtk_p1.png "Matplotlib pressure ")

##### Velocity visualisation in Paraview
![Paraview velocity](sample_images/paraview_U1.png "Paraview velocity")

##### And in matplotlib
![Matplotlib velocity](sample_images/vtk_U1.png "Matplotlib velocity")

### Dynamic velocity visualisation compared to Paraview

##### Velocity visualisation in Paraview
![Paraview velocity in dynamic](sample_images/paraview_velocity.gif "Paraview velocity")

##### And in matplotlib: side panel (Z=0)
![Matplotlib velocity in dynamic](sample_images/out.gif "Matplotlib velocity")

## Execution environment 

Run Jupyter notebook in Docker container.

Build Docker image with included Dockerfile.
Sample data is in VTK folder. Mount this folder into container /openfoam directory. Use `./startcontainer.sh` command.

## Requirements

See Dockerfile for required packages and installation steps on Debian. On Ubuntu installation is very similar, but some package names are different.

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




