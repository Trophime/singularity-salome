SALOME_DIR=$HOME/Salome_Packages/SALOME-9.3.0b2-MPI--DBtesting/
HIFIMAGNET=${SALOME_DIR}/BINARIES-DBtesting/HIFIMAGNET/bin/salome

${SALOME_DIR}/salome -t -m GEOM,SMESH,HIFIMAGNET $HIFIMAGNET/HIFIMAGNET_Cmd.py args:--cfg=Insert-H1H4-Leads-2t.yaml,--air
