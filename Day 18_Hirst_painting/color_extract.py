import colorgram
""" A python package to extract RGB values from a picture"""
colors = colorgram.extract('hirst.jpg', 30)
color_list = []
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    new_color = (r, g, b)
    color_list.append(new_color)
print(color_list)

