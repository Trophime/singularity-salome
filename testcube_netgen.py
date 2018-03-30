# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v8.4.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.NoteBook(theStudy)
sys.path.insert( 0, r'/home/LNCMI-G/trophime/feelpp/research/hifimagnet/singularity/salome')

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
[Face_1,Face_2,Face_3,Face_4,Face_5,Face_6] = geompy.ExtractShapes(Box_1, geompy.ShapeType["FACE"], True)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudyInFather( Box_1, Face_1, 'Face_1' )
geompy.addToStudyInFather( Box_1, Face_2, 'Face_2' )
geompy.addToStudyInFather( Box_1, Face_3, 'Face_3' )
geompy.addToStudyInFather( Box_1, Face_4, 'Face_4' )
geompy.addToStudyInFather( Box_1, Face_5, 'Face_5' )
geompy.addToStudyInFather( Box_1, Face_6, 'Face_6' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New(theStudy)
Mesh_1 = smesh.Mesh(Box_1)
NETGEN_1D_2D_3D = Mesh_1.Tetrahedron(algo=smeshBuilder.NETGEN_1D2D3D)
NETGEN_3D_Simple_Parameters_1 = NETGEN_1D_2D_3D.Parameters(smeshBuilder.SIMPLE)
NETGEN_3D_Simple_Parameters_1.SetNumberOfSegments( 15 )
NETGEN_3D_Simple_Parameters_1.LengthFromEdges()
NETGEN_3D_Simple_Parameters_1.LengthFromFaces()
Box_1_1 = Mesh_1.GroupOnGeom(Box_1,'Box_1',SMESH.VOLUME)
Face_1_1 = Mesh_1.GroupOnGeom(Face_1,'Face_1',SMESH.FACE)
Face_2_1 = Mesh_1.GroupOnGeom(Face_2,'Face_2',SMESH.FACE)
Face_3_1 = Mesh_1.GroupOnGeom(Face_3,'Face_3',SMESH.FACE)
Face_4_1 = Mesh_1.GroupOnGeom(Face_4,'Face_4',SMESH.FACE)
Face_5_1 = Mesh_1.GroupOnGeom(Face_5,'Face_5',SMESH.FACE)
Face_6_1 = Mesh_1.GroupOnGeom(Face_6,'Face_6',SMESH.FACE)
isDone = Mesh_1.Compute()
[ Box_1_1, Face_1_1, Face_2_1, Face_3_1, Face_4_1, Face_5_1, Face_6_1 ] = Mesh_1.GetGroups()


## Set names of Mesh objects
smesh.SetName(NETGEN_1D_2D_3D.GetAlgorithm(), 'NETGEN 1D-2D-3D')
smesh.SetName(NETGEN_3D_Simple_Parameters_1, 'NETGEN 3D Simple Parameters_1')
smesh.SetName(Face_1_1, 'Face_1')
smesh.SetName(Face_2_1, 'Face_2')
smesh.SetName(Face_3_1, 'Face_3')
smesh.SetName(Face_4_1, 'Face_4')
smesh.SetName(Face_5_1, 'Face_5')
smesh.SetName(Face_6_1, 'Face_6')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(Box_1_1, 'Box_1')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(True)
