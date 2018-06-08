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
piston = geompy.ImportSTEP("/home/LNCMI-G/trophime/feelpp/research/hifimagnet/singularity/salome/piston.stp", True, True)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( piston, 'piston' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(True)
