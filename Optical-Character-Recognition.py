import cv2
import matplotlib.pyplot as plt
import easyocr

path = "C:\\Users\\deniz\\Desktop\\text-detection\\Free_Beer.jpg"
img = cv2.imread(path)

reader = easyocr.Reader(['en'])

myText = reader.readtext(img)
print(myText)

minThresholdForDisplay = 0.25

# Yazı boyutu ve kalınlık ayarları
font_scale = 7  # Daha büyük yazı boyutu için artırıldı
font_thickness = 20  # Daha kalın yazı için artırıldı

for numerator, detectedText in enumerate(myText):
    print(detectedText)

    bbox, text, score = detectedText
    pos1 = tuple([int(i) for i in bbox[0]])
    pos2 = tuple([int(i) for i in bbox[2]])

    if score > minThresholdForDisplay:
        cv2.rectangle(img, pos1, pos2, (0, 0, 0), 5)
        # Ayarlanan font boyutu ve kalınlık ile metni çizin
        cv2.putText(img, text, pos1, cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 0, 0), font_thickness)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
