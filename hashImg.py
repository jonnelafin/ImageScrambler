import numpy
#import hashlib
data = numpy.zeros((1024, 1024, 3), dtype=numpy.uint8)
import time

def jpg_image_to_array(image_path):
  from PIL import Image
  """
  Loads JPEG image into 3D Numpy array of shape 
  (width, height, channels)
  """
  with Image.open(image_path) as image:         
    im_arr = numpy.fromstring(image.tobytes(), dtype=numpy.uint8)
    im_arr = im_arr.reshape((image.size[1], image.size[0], 3))                                   
  return im_arr
def mainM(name):
  print("Converting from image...")
  data = jpg_image_to_array("img.jpg")
  x = 0
  y = 0
  z = 0
  r = 0
  c = 0
  print("magik")
  for i in data:
      for p in i:
          for g in p:
              data[x][y][z] = hash(g + (time.localtime().tm_sec / 7)) * g
  ##            data[x][y][z] = (int(hashlib.sha1(g).hexdigest(), 16) % (255))
  #            data[x][y][z] = (int(hashlib.sha1(g / data[x][y][z]).hexdigest(), 1
              z = z + 1
          y = y + 1
          z = 0
      #print(str((len(i)/100)*x))
      x = x + 1
      y = 0
  print("Converting back to image...")
  data[25, 25] = [255, 0, 0]
  data[25, 26] = [0, 255, 0]
  data[25, 27] = [0, 0, 255]

  from PIL import Image

  image = Image.fromarray(data)
  image.save(name)
for i in range(75):
    mainM("nice"+str(i)+".jpg")
print("completed!")
