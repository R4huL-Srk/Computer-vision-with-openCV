import cv2

# Load the source and destination images
source_image = cv2.imread('watermark.png')
destination_image = cv2.imread('data1.jpg')
cv2.imshow("Original image 1", source_image)
cv2.imshow("Original image 2", destination_image)
# Step 1: Crop a region from the source image
# Define the region of interest (ROI) coordinates in the source image
x, y, width, height = 50, 50, 100, 100  # Example coordinates (x, y) and size (width, height)
cropped_image = source_image[y:y + height, x:x + width]  # Crop the selected region

# Step 2: Define where to paste in the destination image
# Specify the top-left corner where the cropped image will be placed in the destination image
paste_x, paste_y = 150, 150

# Check if the cropped area fits within the destination image at the specified location
dest_h, dest_w = destination_image.shape[:2]
if paste_x + width <= dest_w and paste_y + height <= dest_h:
    # Step 3: Paste the cropped image into the destination image
    destination_image[paste_y:paste_y + height, paste_x:paste_x + width] = cropped_image
else:
    print("Cropped area does not fit within the destination image at the specified location.")

# Save and display the result

cv2.imshow('cropped image', cropped_image)
cv2.imshow('Copy and pasted Image', destination_image)  # Show the result
cv2.waitKey(0)
cv2.destroyAllWindows()
