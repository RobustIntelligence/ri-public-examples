import os
import argparse
import subprocess
from typing import List, Optional, Tuple
from pathlib import Path
import requests


GITHUB_URL = "https://raw.githubusercontent.com/RobustIntelligence/ri-public-examples/master/"
DEFAULT_CONFIG_PATH = "configs/stress_test_config.json"


def _download_file(remote_path: str, local_path: Path) -> None:
    """Downloads file to local path."""
    r = requests.get(remote_path)
    with open(local_path, 'wb') as f:
        f.write(r.content)

def _fetch_urls_and_outpaths(remote_file_path: str, out_dir: Path) -> List[Tuple[str, Path]]:
    """Fetch urls and output paths from text file."""
    # TODO: add data_urls/configs to package data directly
    # first download remote file path
    local_path = out_dir / Path(remote_file_path).name
    
    _download_file(remote_file_path, local_path)
    
    urls_and_outpaths = []
    with open(local_path, "r") as fp:
        for line in fp:
            tokens = [t.strip() for t in line.split(',')]
            if len(tokens) != 2:
                raise Exception(
                    "Number of comma-separated values should be 2. "
                    f"Actual: {len(tokens)}"
                )

            urls_and_outpaths.append((tokens[0], Path(tokens[1])))
    return urls_and_outpaths


def _download_files(
    urls_and_outpaths: List[Tuple[str, Path]], out_dir: Path
) -> None:
    """Download files."""
    if not out_dir.exists():
        os.makedirs(out_dir)
    for url, outpath in urls_and_outpaths:
        # if subfolders are specified, create those subfolders
        full_outpath = out_dir / outpath
        out_zip_dir = full_outpath.parent
        _download_file(url, full_outpath)
        # if downloading a zip file, unzip
        if outpath.suffix == ".zip":
            # unzip in parent directory
            subprocess.run(["unzip", "-o", full_outpath, "-d", out_zip_dir])


def _download_configs(
    project_dir: str,
    out_dir: Path,
    config_files: List[str],
) -> None:
    """Download configs."""
    config_urls_and_outpaths = []
    for config_file in config_files:
        remote_config_path = project_dir + "/configs/" + config_file
        config_urls_and_outpaths.append((remote_config_path, Path(config_file)))
    _download_files(config_urls_and_outpaths, out_dir / "configs")


def download_files(
    project_dir: str,
    out_dir: Optional[str] = None,
    config_files: Optional[List[str]] = None
) -> None:
    """Download files from external URL's."""
    if Path(project_dir).is_absolute():
        raise ValueError(
            "project_dir must be a relative path to a directory in the "
            f"ri-public-examples github repo."
        )

    project_dir = os.path.join(GITHUB_URL, project_dir)
    out_dir = Path(out_dir) if out_dir is not None else project_dir
    if not out_dir.exists():
        os.makedirs(out_dir)
    # load in URL's and output paths
    data_urls_and_outpaths = _fetch_urls_and_outpaths(project_dir + "/data_urls.csv", out_dir)
    model_urls_and_outpaths = _fetch_urls_and_outpaths(project_dir + "/model_urls.csv", out_dir)

    # download files
    _download_files(data_urls_and_outpaths, out_dir / "data")
    _download_files(model_urls_and_outpaths, out_dir / "models")

    # download configs if config_paths specified
    if config_files is not None:
        _download_configs(project_dir, out_dir, config_files)
