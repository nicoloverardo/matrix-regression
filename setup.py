from distutils.core import setup
from setuptools import find_packages
import sys

from pathlib import Path  # noqa E402

CURRENT_DIR = Path(__file__).parent
sys.path.insert(0, str(CURRENT_DIR))


def get_long_description() -> str:
    return (
        (CURRENT_DIR / "README.md").read_text(encoding="utf8")
    )


setup(
    name="matrixreg",
    packages=find_packages(),
    version="0.1",
    license="MIT",
    description="Implementation of the MatrixRegression (MR) algorithm for online-learning multi-label text classification, by Popa, Zeitouni & Gardarin",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Nicolò Verardo",
    author_email="n.verardo@outlook.com",
    url="https://github.com/nicoloverardo/matrix_regression",
    download_url="https://github.com/nicoloverardo/matrix_regression/archive/refs/tags/v0.1.tar.gz",
    keywords=["text-classification", "multi-label-classification", "online-learning"],
    install_requires=[
        "numpy>=1.18.5",
        "scipy>=1.4.1",
        "scikit_learn>=0.24.1"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
