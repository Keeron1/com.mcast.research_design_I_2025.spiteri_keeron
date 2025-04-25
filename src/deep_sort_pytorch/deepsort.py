from .deep_sort import build_tracker
import os
import json
import yaml

class DeepSortTracker:
    def __init__(self, cfg, use_cuda=True):
        self.tracker = build_tracker(cfg, use_cuda=use_cuda)

    def update(self, bbox_xywh, confidences, cls_ids, image, seg_masks=None):
        if seg_masks is not None:
            return self.tracker.update(bbox_xywh, confidences, cls_ids, image, seg_masks)
        else:
            return self.tracker.update(bbox_xywh, confidences, cls_ids, image)

    def xyxy_to_tlwh(self, bbox):
        return self.tracker._xyxy_to_tlwh(bbox)
        
