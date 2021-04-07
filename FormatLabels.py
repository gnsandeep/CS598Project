import pandas as pd
from sklearn.model_selection import train_test_split

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


def formatrow(row):
    label_dict = {v:0 for v in labels}
    data = row[['Finding Labels']]
    if data[0].split('|')[0] not in label_dict.keys():
        print("##########CHECK LABELS AGAIN#############")
        print(data[0].split('|')[0])
    label_dict[data[0].split('|')[0]] = 1
    label_dict['Image Index'] = row['Image Index']
    label_dict['Patient ID'] = row['Patient ID']
    return pd.Series(label_dict)

def create_df_csv(dataframe,filename):
    dataframe.to_csv(filename, index=False)

results = pd.read_csv('Data_Entry_2017_v2020.csv')
print("Length of Original Dataset : " , len(results))
print("Original Columns : " ,  results.columns.tolist())


def getFirstClass(row):
    data = row[['Finding Labels']]
    row['FLabel'] = data[0].split('|')[0]
    return row

df_updatedLabel = results.apply(getFirstClass, axis=1)

dfnunqpathalogy = df_updatedLabel.groupby('FLabel')['Image Index'].nunique()
print("Original Class Label count : ", dfnunqpathalogy)

sample_df = df_updatedLabel.sample(frac=0.01, replace=False, random_state=1)
print("Length of Sample Dataset : " , len(sample_df))
print("Sample Class Label count : ", sample_df.groupby('FLabel')['Image Index'].nunique())

df_formatted = sample_df.apply(formatrow, axis=1)

train, test = train_test_split(df_formatted, test_size=0.2, random_state=42, shuffle=True)
print("Length of Sample train Dataset : " , len(train))
print("Length of Sample val Dataset : " , len(test))

#print("Sample Train Class Label count : ", train.groupby('FLabel')['Image Index'].nunique())
#print("Sample Test Class Label count : ", test.groupby('FLabel')['Image Index'].nunique())


create_df_csv(train,"train-small.csv")
create_df_csv(test,"val-small.csv")

