import cv2
import svgwrite

# Load the image and resize
base = cv2.imread('images/bebop.jpg')
w = base.shape[1] // 2
h = base.shape[0] // 2
image = cv2.resize(base, (w, h))

# Convert the image to grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# find contours 
imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cdisplay = cv2.drawContours(image, contours, -1, (0, 255, 0), -1)

#save to svg
with open("path.svg", "w+") as f:
    f.write(f'<svg width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">')

    for c in contours:
        f.write('<path d="M')
        for i in range(len(c)):
            x, y = c[i][0]
            f.write(f"{x} {y} ")
        f.write('" style="stroke:pink"/>')
    f.write("</svg>")


# Display the edges
cv2.imshow('contours', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()