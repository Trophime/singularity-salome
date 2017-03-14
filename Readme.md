To create singularity image form Docker:

sudo singularity create --size 6144 salome-7.8.0.img
sudo singularity --verbose import salome-7.8.0.img docker://trophime/salome-7.8.0:nvidia
