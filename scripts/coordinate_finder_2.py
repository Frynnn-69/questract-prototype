import cv2
import sys

click_points = []
defined_boxes = []
current_mouse_pos = None
needs_redraw = True
WINDOW_NAME = "Questract Coordinate Finder - Section 2"

def mouse_event_handler(event, x, y, flags, params):
    """Menangani logika event mouse dan memperbarui state."""
    global needs_redraw, current_mouse_pos

    current_mouse_pos = (x, y)
    needs_redraw = True

    if event == cv2.EVENT_LBUTTONDOWN:
        click_points.append((x, y))
        print(f"Titik #{len(click_points)} ditandai di: {(x, y)}")

        if len(click_points) == 2:
            x1, y1 = click_points[0]
            x2, y2 = click_points[1]
            box = (min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

            defined_boxes.append(box)
            click_points.clear()

            print("-" * 30)
            print(f"✅ Kotak #{len(defined_boxes)} berhasil dibuat!")
            print(f'   "box": {box[:2]}')
            print("-" * 30)

if len(sys.argv) > 1:
    IMAGE_PATH = sys.argv[1]
else:
    IMAGE_PATH = 'test_images/template_kuesioner_2.png'

original_image = cv2.imread(IMAGE_PATH)
if original_image is None:
    print(f"Error: Tidak bisa membuka gambar di '{IMAGE_PATH}'")
    sys.exit()

cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
cv2.setMouseCallback(WINDOW_NAME, mouse_event_handler)

print("--- Questract Coordinate Finder v3.0 ---")
print("Tekan 'r' untuk RESET | Tekan 'q' untuk KELUAR.")
print("-" * 30)

while True:
    if needs_redraw:
        display_buffer = original_image.copy()

        for box in defined_boxes:
            x, y, w, h = box
            cv2.rectangle(display_buffer, (x, y), (x + w, y + h), (0, 0, 255), 2)

        for point in click_points:
            cv2.circle(display_buffer, point, 7, (0, 255, 0), -1)

        # Crosshair
        if current_mouse_pos:
            h, w, _ = display_buffer.shape
            cv2.line(display_buffer, (0, current_mouse_pos[1]), (w, current_mouse_pos[1]), (255, 255, 0), 1)
            cv2.line(display_buffer, (current_mouse_pos[0], 0), (current_mouse_pos[0], h), (255, 255, 0), 1)

        cv2.imshow(WINDOW_NAME, display_buffer)
        needs_redraw = False

    key = cv2.waitKey(20) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('r'):
        print("--- Semua penandaan di-reset ---")
        click_points.clear()
        defined_boxes.clear()
        needs_redraw = True

cv2.destroyAllWindows()
