# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v8.2.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.NoteBook(theStudy)
# sys.path.insert( 0, r'/home/feelpp/data/FUD5')

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
Cylinder_1 = geompy.MakeCylinderRH(80, 300)
geompy.TranslateDXDYDZ(Cylinder_1, 100, 100, -20)

Cylinder_2 = geompy.MakeCylinder(O, OX, 80, 300)
geompy.TranslateDXDYDZ(Cylinder_2, 0, 100, 100)
Cut_1 = geompy.MakeCutList(Box_1, [Cylinder_1, Cylinder_2], True)

geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( Cylinder_1, 'Cylinder_1' )
geompy.addToStudy( Cut_1, 'Cut_1' )
geompy.addToStudy( Cylinder_2, 'Cylinder_2' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(True)
