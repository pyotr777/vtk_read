import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from vtk.util.numpy_support import vtk_to_numpy
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import vtk

from mpl_toolkits.mplot3d import Axes3D

import os
files = os.listdir("./VTK")
for f in files[:15]:
    print(f)

fname = "damBreak4phaseFine_26"
filename = "./VTK/"+fname+".vtk"
reader = vtk.vtkUnstructuredGridReader()
reader.SetFileName(filename)
reader.Update()
nodes_array = reader.GetOutput().GetPoints().GetData()
data_arrays = reader.GetOutput().GetPointData()
print data_arrays

alpha_air_array = data_arrays.GetArray(6)
#speed_vtk_array = data_arrays.GetArray(1)

nodes = vtk_to_numpy(nodes_array)
aa = vtk_to_numpy(alpha_air_array)
print nodes.shape
print "Nodes:"
print nodes
print aa.shape

merged = np.empty([len(nodes),4])
merged[:,0] = aa
merged[:,1:] = nodes
print merged.shape
print merged
merged_z0 = merged[np.where(merged[:,3] == 0)]
print merged_z0.shape
print merged_z0[:,0]

aa_max = np.amax(merged_z0[:,0])
aa_min = np.amin(merged_z0[:,0])
print("aa: {:12.9f} - {:12.9f}".format(aa_min, aa_max))

# 2d plotting
fig = plt.figure(figsize=(8,6))
#cmap = mpl.cm.plasma
color_map = plt.cm.get_cmap('plasma')
axes = plt.gca()
#axes.set_xlim([-.1,2.1])
#axes.set_ylim([-.01,0.11])
#plt.axis('off')
sc = plt.scatter(merged_z0[:,1],merged_z0[:,2],
                 s=320,
#                 color=cmap(p / p_max),
                 c = merged_z0[:,0],
                 cmap = color_map,
                 linewidth='0',
                 marker="s")
plt.colorbar(sc)
fig.tight_layout()
plt.savefig(fname + ".png",bbox_inches='tight')

