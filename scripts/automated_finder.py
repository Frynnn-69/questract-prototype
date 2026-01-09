import cv2
from boxdetect import pipelines, config
import sys

# Configuration
IMAGE_PATH = 'test_images/template_kuesioner_base.png'

print("Starting automated checkbox detection...")

img = cv2.imread(IMAGE_PATH, cv2.IMREAD_COLOR)

if img is None:
    print(f"Error: Cannot open image at '{IMAGE_PATH}'")
else:
    try:
        cfg = config.PipelinesConfig()
        cfg.width_range = (20, 40)
        cfg.height_range = (20, 40)
        cfg.scaling_factors = [1.0]
        cfg.wh_ratio_range = (0.8, 1.2)
        cfg.dilation_iterations = 0

        print("Configuration set. Running detection...")

        checkboxes = pipelines.get_checkboxes(img, cfg=cfg, plot=False)

        print(f"Detection complete. Found {len(checkboxes)} candidate boxes.")

        out_img = img.copy()

        # Extract coordinates from detection results
        # checkboxes is a list of tuples: (coordinates, flag, image_crop)
        # We only need the first element (coordinates)
        for item in checkboxes:
            box = item[0]  # Extract coordinate tuple (x, y, w, h)
            x, y, w, h = box
            cv2.rectangle(out_img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow("Detection Results - Press 'q' to exit", out_img)
        print("Press 'q' on the image window to close.")

        while True:
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"\n--- ERROR ---\nType: {type(e).__name__}\nMessage: {e}\n-------------")
