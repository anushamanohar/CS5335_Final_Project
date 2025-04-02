import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

from visualize import Visualizer


class waypoints_generator():
    def _generate_text_image(self, text, font_path='interbotix_ws/venv/lib/python3.9/site-packages/cv2/qt/fonts/DejaVuSans-Bold.ttf', font_size=20):
        # Create an image from the text
        font = ImageFont.truetype(font_path, font_size)
        img = Image.new('L', (300, 100), color=255)  # 'L' mode is grayscale
        draw = ImageDraw.Draw(img)
        draw.text((10, 10), text, font=font, fill=0)
        
        return np.array(img)

    def _get_contours_from_image(self, img):
        # Convert image to binary (black and white)
        _, binary = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
        
        # Find contours
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        return contours

    def _convert_contours_to_waypoints(self, contours):
        # Convert contours to waypoints
        waypoints = []
        for contour in contours:
            for point in contour:
                # Extract x, y coordinates from contour
                x, y = point[0]
                waypoints.append((x / 100.0, y / 100.0))  # Scale down coordinates for robot arm
        return waypoints

    def get_waypoints(self, text):
        # Generate image with text
        img = self._generate_text_image(text)
        
        
        # Get contours from the image
        contours = self._get_contours_from_image(img)
        
        # Convert contours to waypoints
        waypoints = self._convert_contours_to_waypoints(contours)
        
        return waypoints
    

if __name__ == '__main__':
    text = 'A'
    obj = waypoints_generator()
    waypoints = obj.get_waypoints(text)

    img = obj._generate_text_image(text)
    vis_obj = Visualizer()
    vis_obj.visualize_img(img)

    vis_obj.visualize_waypoints(waypoints)



