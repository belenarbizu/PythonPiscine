from load_image import ft_load
from scipy import ndimage, misc


def zoom(path):
    print(ft_load(path))
    try:
        img = cv2.imread(path)
    except:
        print("Error")


def main():
    zoom("animal.jpeg")


if __name__ == "__main__":
    main()
