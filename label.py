import cv2


def draw_labels(image_path, label_path, output_path):
    # 讀取圖片
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to load image {image_path}")
        return

    H, W, _ = image.shape

    # 讀取標籤文件
    labels = []
    with open(label_path, 'r') as file:
        for line in file:
            labels.append([float(x) if i > 0 else int(x)
                          for i, x in enumerate(line.strip().split())])

    # 繪製標籤框
    for label in labels:
        class_id, x_center, y_center, width, height = label
        x_center_pixel = int(x_center * W)
        y_center_pixel = int(y_center * H)
        width_pixel = int(width * W)
        height_pixel = int(height * H)

        # 計算左上角和右下角座標
        x1 = int(x_center_pixel - width_pixel / 2)
        y1 = int(y_center_pixel - height_pixel / 2)
        x2 = int(x_center_pixel + width_pixel / 2)
        y2 = int(y_center_pixel + height_pixel / 2)

        # 繪製矩形框
        color = (0, 255, 0) if class_id == 0 else (0, 0, 255)  # 不同類別不同顏色
        cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)

    # 保存並顯示圖片
    cv2.imwrite(output_path, image)
    print(f"Labeled image saved as {output_path}")
    cv2.imshow('Image with Labels', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 使用範例
image_path = './demo_tomato/images/train/10.jpg'  # 輸入圖片的路徑
label_path = './demo_tomato/labels/train/10.txt'  # 輸入標籤文件的路徑
output_path = './label/labeled_image10.jpg'  # 輸出圖片的路徑

draw_labels(image_path, label_path, output_path)
