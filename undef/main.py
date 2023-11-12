from deepface import DeepFace


def face_verify(img1, img2):
    try:
        result_dict = DeepFace.verify(img1_path=img1, img2_path=img2, enforce_detection=False)
        return result_dict
    except Exception as _ex:
        return _ex


def main():
    print(face_verify(img1='img/new_foto8.png', img2='img/um.jpg'))


if __name__ == '__main__':
    main()
