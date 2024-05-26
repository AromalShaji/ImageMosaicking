import numpy as np
import cv2
import matplotlib.pyplot as plt

def perform_mosaicking(img1, img2):
 
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    
  
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)
    
    
    if len(good_matches) > 4:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        
        height, width, _ = img2.shape
        img1_warp = cv2.warpPerspective(img1, H, (width, height))
        
        
        result = cv2.addWeighted(img1_warp, 0.5, img2, 0.5, 0)
        return result
    else:
        return None

if __name__ == '__main__':
    img1 = cv2.imread('/content/img1.jpg')
    img2 = cv2.imread('/content/img2.jpg')

    result = perform_mosaicking(img1, img2)
    if result is not None:
        plt.imshow(result[:, :, ::-1])
        plt.show()
    else:
        print('Unable to form a mosaic')
