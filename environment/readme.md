# Environment

![Build & Publish Docker](https://github.com/related-sciences/string-protein-network/workflows/Build%20&%20Publish%20Docker/badge.svg)

[`requirements.txt`](requirements.txt) specifies the Python dependencies for this repository.

GitHub Actions will automatically build and publish to this repo's [package registry](https://github.com/related-sciences/string-protein-network/packages), when the source for the image changes.
Therefore, you do not need to build the image locally.
However, if you'd like to for development, run the following command with this directory as your current working directory:

```shell
# Build the Docker image specified by Dockerfile (from repo root)
docker build --tag docker.pkg.github.com/related-sciences/string-protein-network/string-protein-network environment
```

If you'd like to evaluate changes to the requirements in a currently running container,
you can run the following command (from the repository's root directory):

```shell
docker exec string-protein-network \
  pip install --upgrade --requirement environment/requirements.txt
```

Open an interactive shell inside a running container,
as the root user to allow systems administration.

```shell
docker exec --interactive --tty --user=root \
  string-protein-network bash
```
