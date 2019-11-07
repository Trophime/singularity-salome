SALOME_DIR=/opt/SALOME-9.3.0-DB10
HIFIMAGNET=${SALOME_DIR}/BINARIES-DB10/HIFIMAGNET/bin/salome

salome -w1 -t -m GEOM,SMESH,HIFIMAGNET $HIFIMAGNET/HIFIMAGNET_Cmd.py args:--cfg=Insert-H1H4-Leads-2t.yaml[,--air,--infty_Rratio=1.2,--infty_Zratio=1.2]
salome -w1 -t -m GEOM,SMESH,HIFIMAGNET $HIFIMAGNET/HIFIMAGNET_Cmd.py args:--cfg=Insert-H1H4-Leads-2t.yaml[,--mesh,--quadratic]
