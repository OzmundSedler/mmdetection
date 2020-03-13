from .builder import build_dataset
from .cityscapes import CityscapesDataset
from .coco import CocoDataset
from .custom import CustomDataset
from .dataset_wrappers import ConcatDataset, RepeatDataset
from .loader import DistributedGroupSampler, GroupSampler, build_dataloader
from .registry import DATASETS
from .voc import VOCDataset
from .wider_face import WIDERFaceDataset
from .xml_style import XMLDataset
<<<<<<< HEAD
<<<<<<< HEAD
from .my_dataset import MyDataset
=======
>>>>>>> parent of 07bd37d... [update_dataset_docs]
=======
>>>>>>> parent of 07bd37d... [update_dataset_docs]

__all__ = [
    'CustomDataset', 'XMLDataset', 'CocoDataset', 'VOCDataset',
    'CityscapesDataset', 'GroupSampler', 'DistributedGroupSampler',
    'build_dataloader', 'ConcatDataset', 'RepeatDataset', 'WIDERFaceDataset',
<<<<<<< HEAD
<<<<<<< HEAD
    'DATASETS', 'build_dataset',"MyDataset"
=======
    'DATASETS', 'build_dataset'
>>>>>>> parent of 07bd37d... [update_dataset_docs]
=======
    'DATASETS', 'build_dataset'
>>>>>>> parent of 07bd37d... [update_dataset_docs]
]
