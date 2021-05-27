# import library for getting picture and removing it
import os
import requests
# import library for building api
from fastapi import Request, FastAPI
# import library for ml
import numpy as np
from requests.api import request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# load machine learning models
model = load_model("model/skin_cancer.h5")
model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# convert to decimal method
def decimal_str(x: float, decimals: int = 10) -> str:
    return format(x, f".{decimals}f").lstrip().rstrip('0')

# method for getting picture from internet then putting it on dump folder
def getPics(pics_url):
    pics_path = "dump/"+os.path.basename(pics_url)
    rImg = requests.get(pics_url)
    with open(pics_path, "wb") as f:
        f.write(rImg.content)
    return pics_path

# method for processing the picture to machine learning
def procPics(pics_path: str):
    dataArr = []
    test_img = image.load_img(pics_path, target_size=(224,224))
    test_img = image.img_to_array(test_img)
    test_img = np.expand_dims(test_img, axis=0)
    result = model.predict(test_img)
    for res in result[0]:
        dataArr.append(decimal_str(res))
    os.remove(pics_path)
    return dataArr

# setup fastapi
app = FastAPI()

# post method to activate ml method
@app.post("/ml")
async def getPost(req: Request):

    data = await req.json()

    the_path = getPics(data["url"])
    resData = procPics(the_path)

    return { "res": {
        "akiec": resData[0],
        "bcc": resData[1],
        "bkl": resData[2],
        "df": resData[3],
        "mel": resData[4],
        "nv": resData[5],
        "vasc": resData[6],
    } }