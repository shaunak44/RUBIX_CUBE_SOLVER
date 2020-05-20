from PIL import Image, ImageDraw
im = Image.new('RGB', (300, 300), (255, 128, 128))
draw = ImageDraw.Draw(im)
draw.rectangle((0, 0, 100, 100), fill = (255, 0, 0), outline = (0, 0, 0))
draw.rectangle((100, 0, 200, 100), fill = (0, 192, 192), outline = (0, 0, 0))
draw.rectangle((200, 0, 300, 100), fill = (0, 192, 192), outline = (0, 0, 0))
draw.rectangle((0, 100, 100, 200), fill = (0, 192, 192), outline = (0, 0, 0))
draw.rectangle((100, 100, 200, 200), fill = (0, 192, 192), outline = (0, 0, 0))
draw.rectangle((200, 100, 300, 200), fill = (0, 192, 192), outline = (0, 0, 0))
draw.rectangle((0, 200, 100, 300), fill = (0, 192, 192), outline = (0, 0, 0))
draw.rectangle((100, 200, 200, 300), fill = (0, 192, 192), outline = (0, 0, 0))
draw.rectangle((200, 200, 300, 300), fill = (0, 192, 192), outline = (0, 0, 0))
im.show(draw)

