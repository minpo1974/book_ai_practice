import sys, os
from PIL import Image
import numpy as np
import P00101 as gyudon

if len(sys.argv) <= 1:
    print("python P00102.py image_name image_name .....")
    quit()
image_size = 50

categories = ["일반 규동", "생강 규동", "양파 규동", "치즈 규동"]
calories = [656, 658, 768, 836]

X = []
files = []

for fname in sys.argv[1:]:
    #print(fname)
    img = Image.open(fname)
    img = img.convert("RGB")
    img = img.resize((image_size, image_size))
    in_data = np.asarray(img)
    X.append(in_data)
    files.append(fname)

X = np.array(X)

model = gyudon.build_model(X.shape[1:])
model.load_weights("./image/gyudon-model3.hdf5")

html = ""
pre = model.predict(X)
for i, p in enumerate(pre) :
    y = p.argmax()
    print("+입력:", files[i])
    print("|규동 이름:", categories[y])
    print("|칼로리:", calories[y])
    html += """
        <h3>입력:{0}</h3>
        <div>
          <p><img src="{1}" width=300></p>
          <p>규동 이름:{2}</p>
          <p>칼로리 :{3}kcal</p>
        </div>
    """.format(os.path.basename(files[i]),
        files[i],
        categories[y],
        calories[y])

html = "<html><body style='text-align:center;'>" + \
    "<style> p { margin:0; padding:0; } </style>" + \
    html + "</body></html>"

with open("gyudon-result1.html", "w") as f:
    f.write(html)