import os
import nibabel as nib
import numpy as np
import pandas as pd
from joblib import Parallel, delayed
import argparse

def SUVmax(im, seg, chls = None):
    im_seg = im*seg
    if chls != None:
        if len(chls)==1:
            im_seg = im_seg[:,:,chls[0]]
        elif len(chls)==2:
            ch1, ch2 = chls[0], chls[1] + 1
            im_seg = im_seg[:,:, ch1:ch2 ]
    return np.max( im_seg )

def MTV_TLG_xyz(im, seg, thresh, chls = None, xyz=1):
    im_seg = im*seg
    if chls != None:
        if len(chls)==1:
            im_seg = im_seg[:,:,chls[0]]
        elif len(chls)==2:
            ch1, ch2 = chls[0], chls[1] + 1
            im_seg = im_seg[:,:, ch1:ch2 ]
    MTV = np.sum(im_seg >= thresh)*xyz
    MTV_mean = np.mean(im_seg[im_seg >= thresh]) if im_seg[im_seg >= thresh].size > 0 else 0
    TLG = MTV*MTV_mean if MTV!=0 else 0
    return (MTV, TLG)

def MTV_TLG_mix(im, seg_pet, seg_ct, thresh, chls = None, perc = 0.8):
    im_seg_pet = im*seg_pet
    im_seg_ct = im*seg_ct
    if chls != None:
        if len(chls)==1:
            im_seg = im_seg_pet[:,:,chls[0]]
        elif len(chls)==2:
            ch1, ch2 = chls[0], chls[1] + 1
            im_seg = im_seg_pet[:,:, ch1:ch2 ]
    MTV = np.min((np.sum(im_seg >= thresh), perc*np.sum(im_seg_ct >= 0)))
    MTV_mean = np.mean(im_seg[im_seg >= thresh])
    TLG = MTV*MTV_mean if MTV!=0 else 0
    return (MTV, TLG)

def SUVpeak(im, seg, chls = None):
    im_seg = im*seg
    #separate only nonzero values
    if chls != None:
        if len(chls)==1:
            im_seg = im_seg[:,:,chls[0]]
        elif len(chls)==2:
            ch1, ch2 = chls[0], chls[1] + 1
            im_seg = im_seg[:,:, ch1:ch2 ]
    im_seg = im_seg[im_seg!=0]
    return np.mean( im_seg )




mrn_not_worked = []
def processInput(i,root_dir_Seg, all_col, suv_file_name, seg_file_name, list_of_patients):
    df = pd.DataFrame(columns=all_col)
    folder_name = list_of_patients[i]
    try: 
        path_SUV  = os.path.join(root_dir_Seg, folder_name,suv_file_name)
        path_tumor = os.path.join(root_dir_Seg, folder_name,seg_file_name)

        tumor_h = nib.load(path_tumor)
        SUV_h = nib.load(path_SUV)

        x,y,z = np.diag(np.abs(SUV_h.affine))[0:3]
        xyz = x*y*z

        tumor_seg_pet = tumor_h.get_fdata()
        SUV = SUV_h.get_fdata()

        # tumor volume
        tumor_pix = np.sum(tumor_seg_pet)
        tumor_vol = tumor_pix * xyz

        ch1, ch2 = 0, SUV.shape[2]          #  We take all the slides(channels)
        chls = [ch1, ch2]

        MTV_1_5_V, TLG_1_5_V = MTV_TLG_xyz(SUV, tumor_seg_pet, thresh=1.5, chls= chls, xyz=xyz)
        MTV_2_5_V, TLG_2_5_V = MTV_TLG_xyz(SUV, tumor_seg_pet, thresh=2.5, chls= chls, xyz=xyz)

        SUV_max = SUVmax(SUV, tumor_seg_pet, chls = chls)
        SUV_peak = SUVpeak(SUV, tumor_seg_pet, chls = chls)

        data = [folder_name, MTV_1_5_V, TLG_1_5_V, MTV_2_5_V, TLG_2_5_V, SUV_max ,SUV_peak, tumor_vol, xyz]
        new_row = pd.DataFrame([data], columns=all_col)
        df = pd.concat([df, new_row], ignore_index=True)

        print('{}. {} added!'.format(i, folder_name),"")
        return df
        
    except Exception as e:
        mrn_not_worked.append(folder_name)
        print(f"Error processing {folder_name}: {str(e)}")



def main():
    parser = argparse.ArgumentParser(description="Process PET/CT imaging data.")
    parser.add_argument('--folder', type=str, default='test', help='Folder name for data')
    parser.add_argument('--root_dir', type=str, default='/Data/Mori/others_data/xxxx/', help='Root directory for segment files')
    parser.add_argument('--suv_file', type=str, default='PET.nii', help='Filename for SUV data')
    parser.add_argument('--seg_file', type=str, default='Seg.nii', help='Filename for segmentation data')
    parser.add_argument('--num_cores', type=int, default=4, help='Number of cores to use for parallel processing')
    args = parser.parse_args()

    root_dir_Seg = os.path.join(args.root_dir, args.folder)
    all_col = ['MRN','MTV_1.5', 'TLG_1.5','MTV_2.5', 'TLG_2.5','SUV_max', 'SUV_mean','Tumor_vol','xyz']
    list_of_patients =  [ i for i in os.listdir(root_dir_Seg)  ]

    inputs = range(len(list_of_patients))
    num_cores = min(args.num_cores, len(inputs))
    dfs = Parallel(n_jobs=num_cores)(delayed(processInput)(i, root_dir_Seg, all_col, args.suv_file, args.seg_file, list_of_patients) for i in inputs)
    df = pd.concat(dfs, ignore_index=True)
    output_file = os.path.join(args.root_dir, args.folder + '.csv')
    df.to_csv(output_file)
    print(f"Output saved to {output_file}")

if __name__ == '__main__':
    main()


#python mtv_tlg_main.py --folder test --root_dir /Data/Mori/others_data/mori/ --suv_file PET.nii --seg_file Seg.nii

