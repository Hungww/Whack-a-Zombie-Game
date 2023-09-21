from PIL import Image, ImageDraw, ImageFont
import os
image_folder=os.path.join(os.path.dirname(__file__))
new_image=Image.open(os.path.join(image_folder,"bg2.jpg"))

grave1= new_image.crop((190,427,435,697))
grave1.save(os.path.join(image_folder,"grave1.png"))


grave2= new_image.crop((485,349,615,525))
grave2.save(os.path.join(image_folder,"grave2.png"))


grave3= new_image.crop((737,317,831,531))
grave3.save(os.path.join(image_folder,"grave3.png"))


grave4= new_image.crop((878,550,1080,700))
grave4.save(os.path.join(image_folder,"grave4.png"))


grave5= new_image.crop((896,305,971,390))
grave5.save(os.path.join(image_folder,"grave5.png"))
grave5.show()