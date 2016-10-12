FROM debian:jessie

MAINTAINER Bryzgalov Peter <peterbryz@yahoo.com>

# Install Python and Jupyter, ffmpeg and python-VTK

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    checkinstall bzip2 ca-certificates sudo locales \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y gfortran && apt-get -y autoremove

RUN echo "deb http://www.deb-multimedia.org jessie main non-free" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y --force-yes deb-multimedia-keyring
RUN apt-get update

RUN apt-get install -y libtiff5-dev libjpeg-dev ffmpeg && apt-get -y autoremove
RUN apt-get install -y build-essential libmp3lame-dev libvorbis-dev libtheora-dev \
    libspeex-dev yasm pkg-config libfaac-dev libopenjpeg-dev libx264-dev && apt-get -y autoremove

RUN apt-get install -y python-setuptools python-pip && apt-get -y autoremove
RUN apt-get install -y python-matplotlib python-numpy python-scipy python-pandas \
    python-tk && apt-get -y autoremove

RUN apt-get install -y libvtk5-dev libvtk5.8 && apt-get -y autoremove
RUN apt-get install -y python-vtk python-pyvtk && apt-get -y autoremove

RUN /usr/bin/python --version

RUN pip install -U pip
RUN pip install nose
RUN pip install "ipython[notebook]"
RUN pip install -U matplotlib
RUN pip install -U Pillow

WORKDIR /root

CMD "jupyter notebook --no-browser --ip=0.0.0.0"