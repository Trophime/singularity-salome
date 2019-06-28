= To create singularity image from Docker Official Salome images:

Supported Versions: `7.8.0` to `8.4.0`
Supported Graphic card: `nvidia`, `intelhd`


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

Note: `--writable is need for cesga`

An alternative is to build the image using the Salome binairies, for details see recipe
```
sudo -E singularity -vvv build --force --notest [--writable] "./salome-$VERSION-$TAG.simg" "./stretch.def"
```

!! Watch out for kernel limitations when using latest Debian/Ubuntu releases !!
(eg on cesga Ubuntu 18.04 LTS images won't run, same for Debian buster)

= Upload singularity image to cesga registry:

```
export SREGISTRY_CLIENT=registry
export SREGISTRY_CLIENT_SECRETS=~/.sregistry-cesga
[export SREGISTRY_STORAGE=...]

sregistry push --name hifimagnet/salome --tag 8.4.0 salome-8.4.0.simg 
```

= Download from cesga sregistry:

```
export SREGISTRY_CLIENT=registry
export SREGISTRY_CLIENT_SECRETS=~/.sregistry-cesga
[export SREGISTRY_STORAGE=...]

sregistry pull --name salome-8.4.0.simg hifimagnet/salome:8.4.0
[sregistry rename hifimagnet/salome:8.4.0 salome-8.4.0.simg]
```

On cesga, as sregistry is not installed you should instead use sregistry-cli image :
```
singularity run -B /mnt shub://sregistry.srv.cesga.es/mso4sc/sregistry pull hifimagnet/salome:8.4.0
singularity run -B /mnt shub://sregistry.srv.cesga.es/mso4sc/sregistry rename hifimagnet/salome:8.4.0 salome-8.4.0.simg 
```

Note that you may reveive somm warnings like that:

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

* build for previous singularity version

```
docker run --privileged -t --rm \
 -v $PWD:/tmp/salome \
 -v /home/LNCMI-G/trophime/Salome_Packages/:/home/LNCMI-G/trophime/Salome_Packages/ \
 singularityware/singularity:2.4  build [-w] /tmp/salome/salome-9.3.0-buster.simg /tmp/salome/buster-9.3.0.def
```

*

```
singularity run shub://sregistry.srv.cesga.es/mso4sc/sregistry:latest --quiet push --name hifimagnet/salome --tag 9.3.0 salome-9.3.0-buster.simg
```
