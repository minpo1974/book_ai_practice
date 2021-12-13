import piskle

lr = piskle.load('model.pskl')

pre_y = lr.predict([[26.5, 27.8,26.9,26.8,26.5,26.8]])

print([26.5, 27.8,26.9,26.8,26.5,26.8])
print(pre_y)