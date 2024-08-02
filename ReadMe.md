# Running the code
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
