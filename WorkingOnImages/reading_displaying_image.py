import cv2

# reading the image
image = cv2.imread(filename=r'.\img\nature.jpg')

# displaying image
# window name
# image matrix - image varoable
cv2.imshow('My pic', image)

cv2.waitKeyEx(0)
cv2.destroyAllWindows()