# redcap-image-processing

## Overview

The goal of this repository is to explore processing of the output data from a REDCap survey using the [Image Annotator](https://github.com/brown-ccv/redcap-image-annotator) external module.

This repo includes:

- `envs`: anaconda environment YML files
- `notebooks`: jupyter notebooks for post processing
- `src`: miscellaneous scripts for data processing

This repo does not include, and will be stored on the shared drive, is:

- `redcap-api-examples`: examples of how to use REDCap's API
- `data`: miscellaneous data used

What's not included, and will not be stored on the shared drive, is the `validation.env` file that stores the API tokens and urls for the validation server. If you are needing to use REDCap's API on any server other than your local development, contact your REDCap admin.

## Development Environment

[Anaconda](https://www.anaconda.com/) is mainly used for package management. For development, you'll need to [install Anaconda](https://docs.anaconda.com/anaconda/install/).

To build and activate the conda environment, run the following command lines:

```
conda env create -f envs/rdc_img_proc.yml -n rdc_img_proc
conda activate rdc_img_proc
```

For more on managing conda environments, see [this](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

## Using Scripts/Notebooks

Before using the notebooks, you'll need to activate the conda development environment (see above).

The `notebooks/image_annotation_processing.ipynb` notebook attempts to recreate the annotation overlayed with the uploaded image. It uses a dataset created from a simple survey on REDCap stored in `data`.

The `notebooks/validate_annotation.ipynb` notebook attempts to validate that a single annotation is overlayed with the area annotation. This notebook will not fully work unless you have access to REDCap's validation server with API credentials. If you need API credentials, contact your REDCap admin.

For more on using jupyter notebooks, see its documentation [here](https://docs.jupyter.org/en/latest/).

The script `src/test_api.py` tests the API used for the validation server. If you have API credentials stored in an `.env` file, you can use this script by runing the following command after changing the config path pointing to the `.env` file:

```
python src/test_api.py
```

For more information about the full scope of this project, see the google drive documentation [here](https://drive.google.com/drive/folders/1-8i5lYVyXLfATh6kyM-_EwJ_JkCmnAYf?usp=sharing).