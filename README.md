# EC7212 - Computer Vision and Image Processing

## Take Home Assignment 1

### Student Information

* **Name**: Amarasinghe WLSK
* **Reg No**: EG/2019/3818

---

## 🔧 Project Structure

```
ec7212-basic-image-processing-ops/
├── Q1_Intensity_Reduction/
│   ├── q1_intensity_levels.py
│   └── Q1_output/
├── Q2_Spatial_Averaging/
│   ├── q2_averaging_filter.py
│   └── Q2_output/
├── Q3_Image_Rotation/
│   ├── q3_image_rotation.py
│   └── Q3_output/
├── Q4_Block_Averaging/
│   ├── q4_block_average.py
│   └── Q4_output/
├── test_image.jpg
├── requirements.txt
└── README.md
```

---

## 📦 Requirements

Before running the scripts, make sure to install dependencies:

```bash
pip install -r requirements.txt
```

**requirements.txt**:

```
opencv-python
numpy
```

---

## 🧪 How to Run Each Question

Place a test image named `test_image.jpg` in the root folder before executing the scripts.

### ✅ Question 1 - Intensity Level Reduction

```bash
python Q1_Intensity_Reduction/q1_intensity_levels.py
```

**Output**: Saved images with different intensity levels in `Q1_output/`

---

### ✅ Question 2 - Spatial Averaging (3x3, 10x10, 20x20)

```bash
python Q2_Spatial_Averaging/q2_averaging_filter.py
```

**Output**: Blurred images saved in `Q2_output/`

---

### ✅ Question 3 - Image Rotation (45°, 90°)

```bash
python Q3_Image_Rotation/q3_image_rotation.py
```

**Output**: Rotated images saved in `Q3_output/`

---

### ✅ Question 4 - Block Averaging (3x3, 5x5, 7x7)

```bash
python Q4_Block_Averaging/q4_block_average.py
```

**Output**: Block-averaged images saved in `Q4_output/`

---


