import cv2
from skimage.metrics import structural_similarity as ssim
img1 = cv2.imread("img1.jpg", 0)
img2 = cv2.imread("img2.jpg", 0)
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
score, diff = ssim(img1, img2, full=True)
similarity_percent = score * 100
diff = (diff * 255).astype("uint8")
print(f"Схожість (SSIM) = {similarity_percent:.2f} %")
