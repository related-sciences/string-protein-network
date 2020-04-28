"""
Copyright 2020 Related Sciences

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import pathlib
import sys
import urllib.request
import typing

import pandas as pd

"""type hint for path-like objects that will passthrough os.fspath."""
PathLike = typing.Union[str, pathlib.Path]


def get_string_dataset_path(
    name: str = "protein.info",
    organism: str = "9606",
    version: str = "v11.0",
    directory: PathLike = "data/string-downloads",
) -> pathlib.Path:
    """
    Return local path to a STRING dataset,
    downloading the file to `directory` if it doesn't already exist.
    """
    filename = f"{organism}.{name}.{version}.txt.gz"
    path = pathlib.Path(directory, filename)
    if not path.exists():
        url = f"https://stringdb-static.org/download/{name}.{version}/{filename}"
        sys.stderr.write(f"Downloading {url} to {path}")
        # Set User-agent so STRING server allows download
        opener = urllib.request.build_opener()
        opener.addheaders = [
            (
                "User-agent",
                "Mozilla/5.0: https://github.com/related-sciences/string-protein-network",
            )
        ]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(url, path)
    return path


def get_protein_info_df() -> pd.DataFrame:
    """
    Return `9606.protein.info.v11.0.txt.gz` as a dataframe.
    Adds an index column for use as zero-indexed matrix lookup.
    """
    gene_path = get_string_dataset_path("protein.info")
    gene_df = pd.read_csv(gene_path, sep='\t')
    gene_df = gene_df.reset_index()
    return gene_df
