from PIL import Image
content = 'D:\Python\Python36\pictures'
img = Image.open(content+'\wechat.jpg')
img.resize((128,128))

#img.save(content+'\wechat_py.png')
#保存为ico格式的图片无法读取
img.save(content+'\wechat_py.ico')
