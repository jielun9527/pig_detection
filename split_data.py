import os
import shutil
import random

src_img = r"C:\Users\jielun\Desktop\pig_test\images"
src_lbl = r"C:\Users\jielun\Desktop\pig_test\labels"
dst_base = r"C:\Users\jielun\Desktop\pig_test\pig_dataset"

train_img = os.path.join(dst_base, "images", "train")
val_img = os.path.join(dst_base, "images", "val")
train_lbl = os.path.join(dst_base, "labels", "train")
val_lbl = os.path.join(dst_base, "labels", "val")

for d in [train_img, val_img, train_lbl, val_lbl]:
    for existing in os.listdir(d):
        fp = os.path.join(d, existing)
        if os.path.isfile(fp):
            os.chmod(fp, 0o777)

for d in [train_img, val_img, train_lbl, val_lbl]:
    os.makedirs(d, exist_ok=True)

images = [f for f in os.listdir(src_img) if f.endswith(('.jpg', '.png', '.gif'))]
total = len(images)
val_count = int(total * 0.2)

random.seed(42)
random.shuffle(images)
val_images = images[:val_count]
train_images = images[val_count:]

copied_train_img = 0
copied_train_lbl = 0
for img in train_images:
    img_path = os.path.join(src_img, img)
    dst_path = os.path.join(train_img, img)
    try:
        shutil.copy2(img_path, dst_path)
        copied_train_img += 1
    except Exception as e:
        print(f"Failed to copy {img}: {e}")
    lbl_name = os.path.splitext(img)[0] + ".txt"
    lbl_path = os.path.join(src_lbl, lbl_name)
    if os.path.exists(lbl_path):
        try:
            shutil.copy2(lbl_path, os.path.join(train_lbl, lbl_name))
            copied_train_lbl += 1
        except Exception as e:
            print(f"Failed to copy label {lbl_name}: {e}")

copied_val_img = 0
copied_val_lbl = 0
for img in val_images:
    img_path = os.path.join(src_img, img)
    dst_path = os.path.join(val_img, img)
    try:
        shutil.copy2(img_path, dst_path)
        copied_val_img += 1
    except Exception as e:
        print(f"Failed to copy {img}: {e}")
    lbl_name = os.path.splitext(img)[0] + ".txt"
    lbl_path = os.path.join(src_lbl, lbl_name)
    if os.path.exists(lbl_path):
        try:
            shutil.copy2(lbl_path, os.path.join(val_lbl, lbl_name))
            copied_val_lbl += 1
        except Exception as e:
            print(f"Failed to copy label {lbl_name}: {e}")

print(f"Training images: {copied_train_img}")
print(f"Validation images: {copied_val_img}")
print(f"Training labels: {copied_train_lbl}")
print(f"Validation labels: {copied_val_lbl}")
