from PIL import ImageDraw, Image, ImageFont


font = ImageFont.truetype(
    'T:\Desktop\Time Machine\Poppins\Poppins-ExtraBold.ttf', 50)
for i in range(10):
    image = Image.new('RGB', (50, 50), '#49474E')
    drawer = ImageDraw.Draw(image)
    drawer.text((13, -8), f'{i}', fill='white', font=font)
    image.save(f'{i}.jpg')
