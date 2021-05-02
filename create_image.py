import cv2 as cv
import numpy as np
from PIL import Image
import random
import os

class CvOverlayImage(object):
    """
    [summary]
      OpenCV形式の画像に指定画像を重ねる
    """

    def __init__(self):
        pass

    @classmethod
    def overlay(
            cls,
            cv_background_image,
            cv_overlay_image,
            point,
    ):
        """
        [summary]
          OpenCV形式の画像に指定画像を重ねる
        Parameters
        ----------
        cv_background_image : [OpenCV Image]
        cv_overlay_image : [OpenCV Image]
        point : [(x, y)]
        Returns : [OpenCV Image]
        """
        overlay_height, overlay_width = cv_overlay_image.shape[:2]

        # OpenCV形式の画像をPIL形式に変換(α値含む)
        # 背景画像
        cv_rgb_bg_image = cv.cvtColor(cv_background_image, cv.COLOR_BGR2RGB)
        pil_rgb_bg_image = Image.fromarray(cv_rgb_bg_image)
        pil_rgba_bg_image = pil_rgb_bg_image.convert('RGBA')
        # オーバーレイ画像
        cv_rgb_ol_image = cv.cvtColor(cv_overlay_image, cv.COLOR_BGRA2RGBA)
        pil_rgb_ol_image = Image.fromarray(cv_rgb_ol_image)
        pil_rgba_ol_image = pil_rgb_ol_image.convert('RGBA')

        # composite()は同サイズ画像同士が必須のため、合成用画像を用意
        pil_rgba_bg_temp = Image.new('RGBA', pil_rgba_bg_image.size,
                                     (255, 255, 255, 0))
        # 座標を指定し重ね合わせる
        pil_rgba_bg_temp.paste(pil_rgba_ol_image, point, pil_rgba_ol_image)
        result_image = \
            Image.alpha_composite(pil_rgba_bg_image, pil_rgba_bg_temp)

        # OpenCV形式画像へ変換
        cv_bgr_result_image = cv.cvtColor(
            np.asarray(result_image), cv.COLOR_RGBA2BGRA)

        return cv_bgr_result_image

def create_image():
    upload_path = "static/image/upload/" + os.listdir("static/image/upload")[0]
    cv_background_image = cv.imread(upload_path)
    cv_overlay_image = cv.imread(
        "static/image/ninja_hashiru.png",
        cv.IMREAD_UNCHANGED)  # IMREAD_UNCHANGEDを指定しα込みで読み込む
    size = cal_image_size(cv_background_image, cv_overlay_image)
    cv_overlay_image = cv.resize(cv_overlay_image, size)
    
    x=int(random.uniform(10,500))
    y=int(random.uniform(10,500))      
    point = (x, y)

    answer_area_x, answer_area_y = cal_answer_area(size, point)

    image = CvOverlayImage.overlay(cv_background_image, cv_overlay_image,
            point)
    cv.imwrite('static/image/offla-hide.png',image)

    os.remove(upload_path)

    return answer_area_x, answer_area_y

def cal_image_size(bg_img, overlay_img):
    bg_height, bg_width = bg_img.shape[:2]
    overlay_height, overlay_width = overlay_img.shape[:2]

    if bg_height > bg_width:
        new_overlay_width = bg_width * 0.1
        new_overlay_height = new_overlay_width * overlay_height / overlay_width
    else:
        new_overlay_height = bg_height * 0.1
        new_overlay_width = new_overlay_height * overlay_width / overlay_height

    size = (int(new_overlay_height), int(new_overlay_width))
    return size 

def cal_answer_area(size, point):
    area_height, area_width = size
    area_x, area_y = point

    area_range_x = (area_x-area_width*0.7, area_x+area_width*0.7)
    area_range_y = (area_y-area_height*0.7, area_y+area_height*0.7)

    return area_range_x, area_range_y