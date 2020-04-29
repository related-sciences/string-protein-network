# STRING Protein Network

This repository downloads and processes protein interaction data for human genes from [STRING](https://string-db.org/).
Currently, v11.0 of the STRING database is analyzed.
More information on STRING is available in:

> **STRING v11: protein–protein association networks with increased coverage, supporting functional discovery in genome-wide experimental datasets**  
Damian Szklarczyk, Annika L Gable, David Lyon, Alexander Junge, Stefan Wyder, Jaime Huerta-Cepas, Milan Simonovic, Nadezhda T Doncheva, John H Morris, Peer Bork, … Christian von Mering  
*Nucleic Acids Research* (2018-11-22) <https://doi.org/gfz2jr>  
DOI: [10.1093/nar/gky1131](https://doi.org/10.1093/nar/gky1131) · PMID: [30476243](https://www.ncbi.nlm.nih.gov/pubmed/30476243) · PMCID: [PMC6323986](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6323986)

## Datasets

This repository produces the following datasets:

- [`data/score-matrices`](data/score-matrices) contains matrices of scores for each evidence channel.
The rows and columns of these matrices are genes in the same order as the `protein.info` STRING download.

Large files are stored using [Git LFS](https://git-lfs.github.com/).
Properly cloning this repository requires having Git LFS installed.

## License Notice

Files in the [`data`](data) directory are released under a [CC BY 4.0 License](https://creativecommons.org/licenses/by/4.0/).
Files in [`data/string-downloads`](data/string-downloads) were downloaded directly from [STRING](https://string-db.org/).
Other files in `data` have modifications performed by the notebooks in this repository.
Please attribute [STRING](https://string-db.org/) and <https://github.com/related-sciences/string-protein-network> when reusing this data.

All contents of this repository outside of the `data` directory are released under the Apache License Version 2.0, as specified in [`LICENSE.md`](LICENSE.md).

## Development

This repository has a corresponding Docker image with the required dependencies.
See [`environment`](environment) for the Docker image specification.

Note that the following Docker commands have a `--mount` argument to give the Docker container access to files in this repository.
Therefore, any changes to the repository content created while running the Docker container will persist in this directory after the container is stopped.

The Docker image is automatically built and published by a GitHub Action.
Even though this repository is public, GitHub [requires](https://github.community/t5/GitHub-Actions/docker-pull-from-public-GitHub-Package-Registry-fail-with-quot/td-p/32782) authentication to download from its package registry.
Therefore, you will need a GitHub account to pull the image.

Use the following steps to [authenticate](https://help.github.com/en/packages/using-github-packages-with-your-projects-ecosystem/configuring-docker-for-use-with-github-packages#authenticating-to-github-packages) your local docker with your GitHub.
Go to <https://github.com/settings/tokens> and create a new personal access token, selecting only the `read:packages` scope.
You can name the token anything, for example "docker login read-only token".
Then run the following command, substituting your username and token from above:

```shell
docker login --username USERNAME --password TOKEN docker.pkg.github.com
```

### Interactive

For interactive development, run the following command:

```shell
# This command must be run with the repository root as your working directory.
# Requires docker version >= 17.06.
docker run \
  --name string-protein-network \
  --detach --rm \
  --env JUPYTER_TOKEN=jhcyibitimnrsisdstuw \
  --publish 8880:8888 \
  --mount type=bind,source="$(pwd)",target=/user/jupyter \
  docker.pkg.github.com/related-sciences/string-protein-network/string-protein-network
```

Then navigate to the following URL in your browser:
<http://localhost:8880?token=jhcyibitimnrsisdstuw>

You should see a Jupyter Notebook landing page where you can open, edit, and run any of the notebooks.

When you are done, you shutdown the Jupyter notebook server and remove the Docker container by running `docker stop string-protein-network` in a terminal.
