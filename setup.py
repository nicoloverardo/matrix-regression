from distutils.core import setup

setup(
    name="matrixreg",
    packages=["matrixreg"],
    version="0.1",
    license="MIT",
    description="Implementation of the MatrixRegression (MR) algorithm for online-learning multi-label text classification, by Popa, Zeitouni & Gardarin",
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
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
