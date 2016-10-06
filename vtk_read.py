# Saving data into png test

import vtk

reader = vtk.vtkDataSetReader()
case_dir = "VTK"
reader.SetFileName(case_dir + "/ppWall_20.vtk")
#reader.ReadAllScalarsOn()
#reader.ReadAllVectorsOn()
reader.Update()

print reader.GetHeader()

datas=reader.GetOutput()

npoints=datas.GetNumberOfPoints()
ncells = datas.GetNumberOfCells()
#nlines = datas.GetNumberOfLines()
#nscalars=reader.GetNumberOfScalarsInFile()
#nvectors=reader.GetNumberOfVectorsInFile()
# ntensors=reader.GetNumberOfTensorsInFile()

#print "points %d, cells %d, lines %d, scalars %d, vectors %d, tensors %d" % (npoints, ncells, nlines, nscalars, nvectors, ntensors)
print "points %d, cells %d" % (npoints, ncells)

for i in range(npoints):
    print datas.GetPoint(i)

print "Cells:"
for i in range(ncells):
    print datas.GetCell(i)



# create source
source = vtk.vtkSphereSource()
source.SetCenter(0,0,0)
source.SetRadius(5.0)

# mapper
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(source.GetOutputPort())
#mapper.SetInputConnection(source.GetOutput())

# actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)

# color the actor
actor.GetProperty().SetColor(1,0,0) # (R,G,B)

#renWin.Render()

# screenshot code:
#w2if = vtk.vtkWindowToImageFilter()
#w2if.SetInput(renWin)
#w2if.Update()

#writer = vtk.vtkPNGWriter()
#writer.SetFileName("screenshot.png")
#writer.SetInput(w2if.GetOutput())
#writer.Write()