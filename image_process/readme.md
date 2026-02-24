# 🖼️ Working With Images in Python Using Pillow

## 📌 Introduction

**Pillow** is a Python library used to work with images.

It helps you to:

* Open images
* Show images
* Resize images
* Crop images
* Rotate images
* Convert image format
* Add text on image
* And more...

Pillow is the updated version of old **PIL (Python Imaging Library)**.

---

## 📦 Install Pillow

First install Pillow using pip:

```bash
pip install pillow
```

---

## 📥 Import Pillow

In Python, we mostly use `Image` class.

```python
from PIL import Image
```

---

# 🖼️ 1. Open an Image

```python
from PIL import Image

img = Image.open("sample.jpg")
img.show()
```

### ✅ Explanation:

* `Image.open()` → Opens the image file
* `"sample.jpg"` → Image file name
* `img.show()` → Displays the image

---

# 📏 2. Get Image Information

```python
print(img.format)   # Image format (JPEG, PNG)
print(img.size)     # (width, height)
print(img.mode)     # Color mode (RGB, L, etc.)
```

### ✅ Meaning:

* **format** → Type of image
* **size** → Width and height
* **mode** → Color type

  * RGB → Color image
  * L → Black and white

---

# 🔄 3. Resize an Image

```python
resized_img = img.resize((300, 300))
resized_img.show()
```

### ✅ Explanation:

* `(300, 300)` → New width and height
* Returns a new resized image

---

# ✂️ 4. Crop an Image

```python
cropped_img = img.crop((50, 50, 200, 200))
cropped_img.show()
```

### ✅ Explanation:

`crop((left, top, right, bottom))`

* 50 → left position
* 50 → top position
* 200 → right position
* 200 → bottom position

---

# 🔁 5. Rotate an Image

```python
rotated_img = img.rotate(90)
rotated_img.show()
```

### ✅ Explanation:

* `90` → Rotate 90 degree
* Rotate is anti-clockwise

---

# 💾 6. Save an Image

```python
img.save("new_image.png")
```

### ✅ Explanation:

* Saves image in new format
* You can change format (JPEG → PNG)

---

# 🎨 7. Convert Image Mode

```python
gray_img = img.convert("L")
gray_img.show()
```

### ✅ Explanation:

* `"L"` → Convert to grayscale
* `"RGB"` → Convert to color image

---

# ✏️ 8. Draw Text on Image

```python
from PIL import ImageDraw

draw = ImageDraw.Draw(img)
draw.text((50, 50), "Hello", fill="red")

img.show()
```

### ✅ Explanation:

* `ImageDraw.Draw()` → Used to draw on image
* `(50, 50)` → Text position
* `"Hello"` → Text
* `fill="red"` → Text color

---

# 🖌️ 9. Flip Image

```python
flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
flipped_img.show()
```

### ✅ Explanation:

* `FLIP_LEFT_RIGHT` → Mirror image

---

# 📚 Common Image Modes

| Mode | Meaning            |
| ---- | ------------------ |
| RGB  | Red, Green, Blue   |
| L    | Grayscale          |
| RGBA | RGB + Transparency |

---

# 🎯 Small Complete Example

```python
from PIL import Image

img = Image.open("sample.jpg")

print("Format:", img.format)
print("Size:", img.size)
print("Mode:", img.mode)

resized = img.resize((400, 400))
gray = resized.convert("L")

gray.save("output.jpg")
gray.show()
```

---

# 🚀 Summary

Pillow helps you to:

* Open images
* Edit images
* Resize, Crop, Rotate
* Convert format
* Add text
* Save images

It is very useful for:

* Image processing
* Web projects
* Automation
* Data science
