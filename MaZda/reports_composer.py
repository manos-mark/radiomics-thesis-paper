import os, glob
import numpy as np
import json

def organize_files_to_dict(path):
    os.chdir(path)
    reports = glob.glob('*.xls')
    patient_names = []
    files = []

    # Find unique patient names
    for report in reports:
        patient_names.append(report.split('_')[1])
    patient_names = np.unique(patient_names)
    
    for name in patient_names:
        files.append({'name': name, 'images':[], 'rois': [], 'reports': []})

    for report in reports:
        patient_name = report.split('_')[1]
        
        image_slice = patient_name + "_slice_" + report.split('_')[-1].split('.')[0]
        image_slice_file = image_slice + '.dcm'

        roi_slice = patient_name + "_roi_slice_" + report.split('_')[-1].split('.')[0]
        roi_slice_file = roi_slice + '.bmp'

        file = next((file for file in files if file['name'] == patient_name), None)

        if file is not None:
            file['images'].append(image_slice_file)    
            file['rois'].append(roi_slice_file)
            file['reports'].append(report)
        
    return files


def export_json(files):
    with open('files.json', 'w') as fp:
        json.dump(files, fp)

if __name__ == '__main__':
    #path = 'C:\\Users\\manosmark\\Desktop\\radiomic_features\\MaZda\\data\\'
    path = '/home/manos/git/radiomics-features-extraction/MaZda/data'
    
    files = organize_files_to_dict(path)

    export_json(files)
    
    

    
