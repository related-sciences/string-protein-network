FROM python:3.8-slim

# install gcc to resolve https://github.com/giampaolo/psutil/issues/1714
RUN apt-get update && \
    apt-get upgrade --yes && \
    apt-get install --yes \
    curl \
    gcc \
    git

# install snap (Stanford Network Analysis Platform)
RUN curl --silent https://snap.stanford.edu/releases/Snap-5.0-Ubuntu18.04.tgz \
  | tar --extract --gzip --strip=1 --directory=/usr/local/bin

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && \
  pip install --requirement requirements.txt && \
  jupyter nbextension enable --py widgetsnbextension

# jupyter compains if run as root.
RUN useradd --create-home --shell=/bin/bash jupyter
USER jupyter
WORKDIR /user/jupyter

EXPOSE 8888
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser"]
