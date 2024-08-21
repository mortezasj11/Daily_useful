

#  Calculation_MTV_TLG_SUVmax_SUVpeak
<!-- ![MTV and TLG Extraction](/images/MTV.png) -->
<img src="/images/MTV.png" alt="MTV and TLG Extraction" width="300">

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

docker run -it --rm --gpus all --shm-size=150G --user root --cpuset-cpus=200-251 \
-v /rsrch1/ip/msalehjahromi/codes/:/Code \
-v /rsrch7/wulab/:/Data \
--name pix2pix33 pix2pix:latest



2. **Run the analysis:**

## Usage

The script `mtv_tlg_main.py` can be executed with the following command-line arguments to configure its behavior:

- `--num_cores <number>`: Specify the number of cores to use for parallel processing. Example: `10`.
- `--root_dir <path>`: Set the root directory where the data files are located. Example: `/path/to/data/`.
- `--folder <name>`: Specify the subfolder within the root directory that contains the data. Example: `test`.
- `--suv_file <filename>`: Define the filename for the SUV data. Example: `PET.nii`.
- `--seg_file <filename>`: Define the filename for the segmentation data. Example: `Seg.nii`.

### Example Command
```sh
python mtv_tlg_main.py --num_cores 10 --root_dir /path/to/data/ --folder test --suv_file PET.nii --seg_file Seg.nii
```



#  Anonymize_Dicom_files
<img src="/images/anonymize.png" alt="anonymize Dicom" width="300">
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


#  DataAugmentation2D_pytorch
Visualizing 2D data augmentation in pytorch.

<img src="/images/Aug.png" alt="anonymize Dicom" width="300">
