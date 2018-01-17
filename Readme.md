= To create singularity image from Docker Official Salome images:

Supported Versions: `7.8.0` to `8.4.0`
Supported Graphic card: `nvidia`, `intelhd`

Required nvidia-smi to be installed onhost

* for 2.3.1 version:

```
DIST=$(docker run -it --rm trophime/salome-$VERSION:$TAG lsb_release -cs)
sudo singularity create --size 6144 ./salome-$VERSION-$DIST-$TAG.simg
sudo singularity --verbose import ./salome-$VERSION-$DIST-$TAG.simg docker://trophime/salome-$VERSION:$TAG
```

where `VERSION` and `TAG` respectively stand for Salome version and graphics driver.

* for 2.4.1 version and higher:

```
DIST=$(docker run -it --rm trophime/salome-$VERSION:$TAG lsb_release -cs)
sudo -E singularity -vvv build --force --notest [--writable] "./salome-$VERSION-$DIST-$TAG.simg" "./salome-docker.def"
```

= Upload singularity image:


= Running singularity

```
singularity shell [--nv] "./salome-$VERSION-$DIST-$TAG.simg"
```

```
singularity run [--nv] "./salome-$VERSION-$DIST-$TAG.simg"
```

`--nv` option is only valid for 2.4.1 and later.

= TODO

* generate def file from requested version and os
* eventually build requested version is not available
* is graphic driver really needed with latest singularity version?
