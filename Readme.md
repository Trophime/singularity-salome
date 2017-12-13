= To create singularity image from Docker:

Supported Versions: `7.8.0` to `8.4.0`
Supported Graphic card: `nvidia`, `intelhd`

* for 2.3.1 version:

```
DIST=$(docker run -it --rm trophime/salome-$VERSION:$TAG lsb_release -cs)
sudo singularity create --size 6144 ./salome-$VERSION-$DIST-$TAG.img
sudo singularity --verbose import ./salome-$VERSION-$DIST-$TAG.img docker://trophime/salome-$VERSION:$TAG
```

where `VERSION` and `TAG` respectively stand for Salome version and graphics driver.

* for 2.4.1 version and higher:

```
DIST=$(docker run -it --rm trophime/salome-$VERSION:$TAG lsb_release -cs)
sudo -E singularity -vvv build --force --notest [--writable] "./salome-$VERSION-$DIST-$TAG.img" "./salome-docker.def"
```

= Upload singularity image:


= Running singularity

```
singularity shell [--nv] "./salome-$VERSION-$DIST-$TAG.img"
```

```
singularity run [--nv] "./salome-$VERSION-$DIST-$TAG.img"
```

`--nv` option is only valid for 2.4.1 and later.

= TODO

* generate def file from requested version and os
* eventually build requested version is not available
* is graphic driver really needed with latest singularity version?