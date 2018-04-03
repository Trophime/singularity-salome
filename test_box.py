# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v8.1.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
theStudy = salome.myStudy

from memory_profiler import profile
from timeit import default_timer as timer

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New(theStudy)

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Box_1 = geompy.MakeBoxDXDYDZ(200, 200, 200)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Box_1, 'Box_1' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder
smesh_gui = salome.ImportComponentGUI('SMESH')

smesh = smeshBuilder.New(theStudy)
Mesh_1 = smesh.Mesh(Box_1)
Regular_1D = Mesh_1.Segment()
Number_of_Segments_1 = Regular_1D.NumberOfSegments(300)
Quadrangle_2D = Mesh_1.Quadrangle(algo=smeshBuilder.QUADRANGLE)
Hexa_3D = Mesh_1.Hexahedron(algo=smeshBuilder.Hexa)

@profile
def computeMesh(mesh):
    
    t0 = timer()
    isDone = mesh.Compute()
    t1 = timer()

    print "Computed in %.1f s"%(t1-t0)

@profile
def displayMesh(mesh):
    
    t0 = timer()
    entry = salome.ObjectToID(mesh.GetMesh())
    smesh_gui.CreateAndDisplayActor(entry)
    t1 = timer()

    print "Displayed in %.1f s"%(t1-t0)

computeMesh(Mesh_1)
displayMesh(Mesh_1)

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(True)
