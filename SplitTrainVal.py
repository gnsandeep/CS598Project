import pandas as pd
from shutil import copyfile

img1_list_file = "/datadrive/NIHData/img01.txt" 
img2_list_file = "/datadrive/NIHData/img02.txt"
img3_list_file = "/datadrive/NIHData/img03.txt"
img4_list_file = "/datadrive/NIHData/img04.txt"
img5_list_file = "/datadrive/NIHData/img05.txt"
img6_list_file = "/datadrive/NIHData/img06.txt"
img7_list_file = "/datadrive/NIHData/img07.txt"
img8_list_file = "/datadrive/NIHData/img08.txt"
img9_list_file = "/datadrive/NIHData/img09.txt"
img10_list_file = "/datadrive/NIHData/img10.txt"
img11_list_file = "/datadrive/NIHData/img11.txt"
img12_list_file = "/datadrive/NIHData/img12.txt"

img1_list = []
with open(img1_list_file) as f:
    for word in f:
        img1_list.append(word.splitlines()[0])

img1_list = []
with open(img1_list_file) as f:
    for word in f:
        img1_list.append(word.splitlines()[0])


img1_list = []
with open(img1_list_file) as f:
    for word in f:
        img1_list.append(word.splitlines()[0])

img1_list = []
with open(img1_list_file) as f:
    for word in f:
        img1_list.append(word.splitlines()[0])

img2_list = []
with open(img2_list_file) as f:
    for word in f:
        img2_list.append(word.splitlines()[0])        

img3_list = []
with open(img3_list_file) as f:
    for word in f:
        img3_list.append(word.splitlines()[0])

img4_list = []
with open(img4_list_file) as f:
    for word in f:
        img4_list.append(word.splitlines()[0])

img5_list = []
with open(img5_list_file) as f:
    for word in f:
        img5_list.append(word.splitlines()[0])

img6_list = []
with open(img6_list_file) as f:
    for word in f:
        img6_list.append(word.splitlines()[0])

img7_list = []
with open(img7_list_file) as f:
    for word in f:
        img7_list.append(word.splitlines()[0])

img8_list = []
with open(img8_list_file) as f:
    for word in f:
        img8_list.append(word.splitlines()[0])

img9_list = []
with open(img9_list_file) as f:
    for word in f:
        img9_list.append(word.splitlines()[0])

img10_list = []
with open(img10_list_file) as f:
    for word in f:
        img10_list.append(word.splitlines()[0])

img11_list = []
with open(img11_list_file) as f:
    for word in f:
        img11_list.append(word.splitlines()[0])

img12_list = []
with open(img12_list_file) as f:
    for word in f:
        img12_list.append(word.splitlines()[0])        

results = pd.read_csv('train-small.csv')
print("Length of test Dataset : " , len(results))
print("Test dataset Columns : " ,  results.columns.tolist())
train_img_lst = results['Image Index'].tolist()
print("Length of train_img_lst : " , len(train_img_lst))

val_res = pd.read_csv('val-small.csv')
print("Length of val Dataset : " , len(val_res))
print("Val dataset Columns : " ,  val_res.columns.tolist())
val_img_lst = val_res['Image Index'].tolist()
print("Length of val_img_lst : " , len(val_img_lst))


for name in train_img_lst:
    if name in img1_list:
        #print("img1_list contains : " ,name)
        copyfile('/datadrive/NIHData/img01/images/' + name , '/datadrive/NIHData/train/' + name)

    if name in img2_list:
       #print("img2_list contains : " , name)
       copyfile('/datadrive/NIHData/img02/images/' + name , '/datadrive/NIHData/train/' + name)

    if name in img3_list:
       #print("img3_list contains : " , name)
       copyfile('/datadrive/NIHData/img03/images/' + name , '/datadrive/NIHData/train/' + name)

    if name in img4_list:
       #print("img4_list contains : " , name)
       copyfile('/datadrive/NIHData/img04/images/' + name , '/datadrive/NIHData/train/' + name)

    if name in img5_list:
       #print("img5_list contains : " , name)
       copyfile('/datadrive/NIHData/img05/images/' + name , '/datadrive/NIHData/train/' + name)

    if name in img6_list:
       #print("img6_list contains : " , name)
       copyfile('/datadrive/NIHData/img06/images/' + name , '/datadrive/NIHData/train/' + name)

    if name in img7_list:
       #print("img7_list contains : " , name)
       copyfile('/datadrive/NIHData/img07/images/' + name , '/datadrive/NIHData/train/' + name)

    if name in img8_list:
       #print("img8_list contains : " , name)
       copyfile('/datadrive/NIHData/img08/images/' + name , '/datadrive/NIHData/train/' + name)

    if name in img9_list:
       #print("img9_list contains : " , name)
       copyfile('/datadrive/NIHData/img09/images/' + name , '/datadrive/NIHData/train/' + name)

    if name in img10_list:
       #print("img10_list contains : " , name)
       copyfile('/datadrive/NIHData/img10/images/' + name , '/datadrive/NIHData/train/' + name)

    if name in img11_list:
       #print("img11_list contains : " , name)
       copyfile('/datadrive/NIHData/img11/images/' + name , '/datadrive/NIHData/train/' + name)

    if name in img12_list:
       #print("img12_list contains : " , name)
       copyfile('/datadrive/NIHData/img12/images/' + name , '/datadrive/NIHData/train/' + name)



for name in val_img_lst:
    if name in img1_list:
        #print("img1_list contains : " ,name)
        copyfile('/datadrive/NIHData/img01/images/' + name , '/datadrive/NIHData/val/' + name)

    if name in img2_list:
       #print("img2_list contains : " , name)
       copyfile('/datadrive/NIHData/img02/images/' + name , '/datadrive/NIHData/val/' + name)

    if name in img3_list:
       #print("img3_list contains : " , name)
       copyfile('/datadrive/NIHData/img03/images/' + name , '/datadrive/NIHData/val/' + name)

    if name in img4_list:
       #print("img4_list contains : " , name)
       copyfile('/datadrive/NIHData/img04/images/' + name , '/datadrive/NIHData/val/' + name)

    if name in img5_list:
       #print("img5_list contains : " , name)
       copyfile('/datadrive/NIHData/img05/images/' + name , '/datadrive/NIHData/val/' + name)

    if name in img6_list:
       #print("img6_list contains : " , name)
       copyfile('/datadrive/NIHData/img06/images/' + name , '/datadrive/NIHData/val/' + name)

    if name in img7_list:
       #print("img7_list contains : " , name)
       copyfile('/datadrive/NIHData/img07/images/' + name , '/datadrive/NIHData/val/' + name)

    if name in img8_list:
       #print("img8_list contains : " , name)
       copyfile('/datadrive/NIHData/img08/images/' + name , '/datadrive/NIHData/val/' + name)

    if name in img9_list:
       #print("img9_list contains : " , name)
       copyfile('/datadrive/NIHData/img09/images/' + name , '/datadrive/NIHData/val/' + name)

    if name in img10_list:
       #print("img10_list contains : " , name)
       copyfile('/datadrive/NIHData/img10/images/' + name , '/datadrive/NIHData/val/' + name)

    if name in img11_list:
       #print("img11_list contains : " , name)
       copyfile('/datadrive/NIHData/img11/images/' + name , '/datadrive/NIHData/val/' + name)

    if name in img12_list:
       #print("img12_list contains : " , name)
       copyfile('/datadrive/NIHData/img12/images/' + name , '/datadrive/NIHData/val/' + name)


