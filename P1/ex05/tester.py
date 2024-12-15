from load_image import ft_load
import cv2
from pimp_image import ft_invert
from pimp_image import ft_red
from pimp_image import ft_blue
from pimp_image import ft_green
from pimp_image import ft_grey

array = ft_load("landscape.jpg")
print(array)
invert = ft_invert(array)
cv2.imshow('Imagen de entrada', invert)
cv2.waitKey(0)
cv2.destroyAllWindows()
red = ft_red(array)
green = ft_green(array)
blue = ft_blue(array)
grey = ft_grey(array)

print(ft_invert.__doc__)