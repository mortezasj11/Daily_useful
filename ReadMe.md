

# PET/CT Imaging Analysis Tool

## Overview
This tool automates the calculation of Metabolic Tumor Volume (MTV), Total Lesion Glycolysis (TLG), SUVmax, and SUVpeak from PET scan. 
It leverages Python's powerful libraries and parallel processing capabilities to efficiently process large datasets.

## Folder Structure
Ensure your data is organized as follows within the specified root directory:

```
root_dir/
    └── folder/
        ├── Patient1/
        │ ├── PET.nii
        │ └── Seg.nii
        ├── Patient2/
        │ ├── PET.nii
        │ └── Seg.nii
...
```

1. **Docker Support**
```sh
docker run -it --rm --gpus all --shm-size=150G --user $(id -u):$(id -g) --cpuset-cpus=200-251 \
-v /rsrch1/ip/msalehjahromi/codes/:/Code \
-v /rsrch7/wulab/:/Data \
--name pix2pix2 pix2pix:latest
```


2. **Run the analysis:**
```sh
python mtv_tlg_main.py --root_dir /path/to/data/ --folder test --suv_file PET.nii --seg_file Seg.nii
```


#######################################################################################################################



# Anonymize Dicom CT
```sh
python anonymize.py --input_dir "Path to the input" --output_dir "Path to the output directory"
```

## Example
```sh
python anonymize.py --input_dir "/Data/Mori_surgery_cohort" --output_dir "/Data/Mori_surgery_cohort_ananymized"
```
## If you want on only 1 file
```sh
python anonymize.py --input_dir "/Data/Mori_surgery_cohort" --output_dir "/Data/Mori_surgery_cohort_ananymized" --only_one_dir "34"
```

# Docker
## Running the docker
```sh
docker run -it --rm --gpus all --shm-size=150G --user $(id -u):$(id -g) --cpuset-cpus=200-210 \
-v /rsrch1/ip/msalehjahromi/codes/:/Code \
-v /rsrch7/wulab/Mori/:/Data \
--name pix2pix2 pix2pix:latest
```
