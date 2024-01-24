import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


# Inisialisasi VideoCapture
cap = cv2.VideoCapture(0)

# Deteksi wajah
while True:
    ret, frame = cap.read()

    # Deteksi wajah
    faces = cv2.CascadeClassifier("haarcascade_frontalface_default.xml").detectMultiScale(frame, 1.1, 5)

    # Tentukan apakah wajah mengantuk
    for (x, y, w, h) in faces:
        # Cek apakah mata terbuka
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        roi_gray = gray[y:y + h, x:x + w]
        eyes = cv2.CascadeClassifier("haarcascade_eye.xml").detectMultiScale(roi_gray, 1.1, 5)
        if len(eyes) == 0:
            # Mata tertutup
            cv2.putText(frame, "Mengantuk", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        else:
            # Mata terbuka
            cv2.putText(frame, "Tidak mengantuk", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Tambahkan bingkai persegi
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Tampilkan hasil
    cv2.imshow("Hasil", frame)

    # Jika tombol q ditekan, hentikan program
    if cv2.waitKey(1) == ord("q"):
        break

# Tutup VideoCapture
cap.release()
