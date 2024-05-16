# Image Mosaicking using SIFT and RANSAC

This Python script demonstrates how to create a mosaic by stitching two images together using the Scale-Invariant Feature Transform (SIFT) algorithm for keypoint detection and matching, along with the Random Sample Consensus (RANSAC) algorithm for estimating the homography matrix.

## Requirements

- Python 3
- OpenCV (`cv2`)
- NumPy
- Matplotlib

## Installation

You can install the required packages via pip:

```bash
pip install opencv-python numpy matplotlib
```

## Usage

1. **Clone the repository or download the script.**
   
2. **Ensure you have two input images (`img1.jpg` and `img2.jpg`) in the same directory as the script.**
   
3. **Run the script:**

    ```bash
    python mosaicking.py
    ```

## Output
![Mosaic Image](https://github.com/AromalShaji/ImageMosaicking/blob/main/Picture1.jpg)

