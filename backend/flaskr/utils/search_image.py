# Search
from towhee import pipe, ops
import numpy
from pathlib import Path


MODEL = 'vgg16'
DEVICE = None # if None, use default device (cuda is enabled if available)
HOST = 'localhost'
PORT = '19530'
TOPK = 10
DIM = 512 # dimension of embedding extracted, change with MODEL
COLLECTION_NAME = 'image_net_search_engine'
INDEX_TYPE = 'IVF_FLAT'
METRIC_TYPE = 'L2'


def get_max_object(img, boxes):
    if len(boxes) == 0:
        return img
    max_area = 0
    for box in boxes:
        x1, y1, x2, y2 = box
        area = (x2-x1)*(y2-y1)
        if area > max_area:
            max_area = area
            max_img = img[y1:y2,x1:x2,:]
    return max_img


p_yolo = (
    pipe.input('img_path')
        .map('img_path', 'img', ops.image_decode('rgb'))
        .map('img', ('boxes', 'class', 'score'), ops.object_detection.yolov5())
        .map(('img', 'boxes'), 'object', get_max_object)
)


p_search_pre_yolo = (
    p_yolo.map('object', 'vec', ops.image_embedding.timm(model_name=MODEL, device=DEVICE))
            .map('vec', 'vec', lambda x: x / numpy.linalg.norm(x, axis=0))
            .map('vec', ('search_res'), ops.ann_search.milvus_client(
                host=HOST, port=PORT, limit=TOPK,
                collection_name=COLLECTION_NAME))
            .map('search_res', 'pred', lambda x: [str(y[0][1:]) if y[0].startswith('.') else str(y[0]) for y in x])
            .output('img_path', 'pred')
)
