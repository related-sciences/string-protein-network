import pathlib
import sys
import urllib.request
import typing

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
