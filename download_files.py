import os
import argparse
import subprocess
from typing import List, Tuple
from pathlib import Path


def _fetch_urls_and_outpaths(file_path: Path) -> List[Tuple[str, Path]]:
    """Fetch urls and output paths from text file."""
    urls_and_outpaths = []
    with open(file_path, "r") as fp:
        for line in fp:
            tokens = [t.strip() for t in line.split(',')]
            if len(tokens) != 2:
                raise Exception(
                    "Number of comma-separated values should be 2. "
                    f"Actual: {len(tokens)}"
                )

            urls_and_outpaths.append((tokens[0], Path(tokens[1])))
    return urls_and_outpaths


def _download_files(urls_and_outpaths: List[Tuple[str, Path]], parent_dir: Path) -> None:
    """Download files."""
    if not parent_dir.exists():
        os.makedirs(parent_dir)
    for url, outpath in urls_and_outpaths:
        # if subfolders are specified, create those subfolders
        full_outpath = parent_dir / outpath
        outdir = full_outpath.parent
        if not outdir.exists():
            os.makedirs(outdir)
        subprocess.run(["wget", url, "-O", full_outpath])
        # if downloading a zip file, unzip
        if outpath.suffix == ".zip":
            # unzip in parent directory
            subprocess.run(["unzip", "-o", full_outpath, "-d", outdir])
            # assert that the unzipped directory has same name as .zip file
            full_outpath_unzip = outdir / (outpath.stem)
            if not full_outpath_unzip.exists():
                raise Exception(
                    "The unzipped directory must exist at following output path: "
                    f"{full_outpath_unzip}. Original zip path: {full_outpath}."
                )


def download_files(project_dir: Path) -> None:
    """Download files from external URL's."""
    # load in URL's and output paths
    data_urls_and_outpaths = _fetch_urls_and_outpaths(project_dir / "data_urls.csv")
    model_urls_and_outpaths = _fetch_urls_and_outpaths(project_dir / "model_urls.csv")

    # download files
    _download_files(data_urls_and_outpaths, project_dir / "data")
    _download_files(model_urls_and_outpaths, project_dir / "models")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--project-dir", help="Path to project directory", required=True, type=str,
    )
    args = parser.parse_args()
    download_files(Path(args.project_dir))

