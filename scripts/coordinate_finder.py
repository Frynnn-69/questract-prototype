import cv2
import sys

# Path ke gambar yang akan diuji
if len(sys.argv) > 1:
    IMAGE_PATH = sys.argv[1]
else:
    IMAGE_PATH = 'test_images/template_kuesioner_2.jpg'

def click_event(event, x, y, flags, params):
    """Fungsi callback yang akan dijalankan setiap kali ada event mouse."""
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Koordinat (x, y): {x}, {y}")

        # `params['image']` image send -> callback
        cv2.circle(params['image'], (x, y), 5, (0, 0, 255), -1)
        cv2.imshow("Coordinate Finder - Tekan 'q' untuk keluar", params['image'])

img = cv2.imread(IMAGE_PATH)

if img is None:
    print(f"Error: Tidak bisa membuka gambar di '{IMAGE_PATH}'")
    exit()

print("Coordinate Finder (x, y)")
print("q for exit.")

cv2.imshow("Coordinate Finder - Tekan 'q' untuk keluar", img)
cv2.setMouseCallback("Coordinate Finder - Tekan 'q' untuk keluar", click_event, {'image': img})

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
