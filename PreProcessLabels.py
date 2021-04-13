import pandas as pd
from shutil import copyfile

labels = ['Cardiomegaly', 
          'Emphysema', 
          'Effusion', 
          'Hernia', 
          'Infiltration', 
          'Mass', 
          'Nodule', 
          'No Finding',
          'Atelectasis',
          'Pneumothorax',
          'Pleural_Thickening', 
          'Pneumonia', 
          'Fibrosis', 
          'Edema', 
          'Consolidation']


org_df = pd.read_csv('Data_Entry_2017_v2020.csv')
def update_toMClass(row):
    label_dict = {v:0 for v in labels}
    imgname = row['Image Index']
    label_dict['Image Index'] = row['Image Index']
    label_dict['Patient ID'] = row['Patient ID']
    label_lsit = row['Finding Labels'].split('|')
    #print(org_label_lsit[0])
    for label in label_lsit:
        label_dict[label] = 1
        
    return pd.Series(label_dict)

org_df_updated = org_df.apply(update_toMClass,axis=1)
org_df_updated.to_csv("Updated_Data_Entry_2017.csv", index=False)

