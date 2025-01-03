import argparse
import os
import random
import torch
import numpy as np

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

def set_random_seed(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True

set_random_seed(1)

def settings():
    parser = argparse.ArgumentParser(description="Training settings")

    parser.add_argument('--type_number', type=int, default=65,
                        help='小数据集的分类为65,大数据为86')
    parser.add_argument('--no-cuda', action='store_true', default=False,
                        help='Disables CUDA training.')
    parser.add_argument('--fastmode', action='store_true', default=False,
                        help='Validate during training pass.')
    parser.add_argument('--workers', type=int, default=0,
                        help='Number of parallel workers. Default is 0.')
    parser.add_argument('--out_file', required=True,default='result.txt',
                        help='Path to data result file. e.g., result.txt')
    parser.add_argument('--lr', type=float, default=1e-3,
                        help='Initial learning rate. Default is 5e-4.')
    parser.add_argument('--dropout', type=float, default=0.5,
                        help='Dropout rate (1 - keep probability). Default is 0.5.')
    parser.add_argument('--weight_decay', default=5e-4,
                        help='Weight decay (L2 loss on parameters) Default is 5e-4.')
    parser.add_argument('--batch', type=int, default=512,
                        help='Batch size. Default is 512.')
    parser.add_argument('--epochs', type=int, default=100,
                        help='Number of epochs to train. Default is 30.')
    
    parser.add_argument('--network_ratio', type=float, default=1,
                        help='Remain links in network. Default is 1')
    parser.add_argument('--loss_ratio1', type=float, default=1,
                        help='Ratio of task1. Default is 1')
    parser.add_argument('--loss_ratio2', type=float, default=0.2,
                        help='Ratio of task2. Default is 0.1')
    
    # GCN参数
    parser.add_argument('--dimensions', type=int, default=512,
                        help='dimensions of feature. Default is 512.')
    parser.add_argument('--hidden1', default=128,
                        help='Number of hidden units for encoding layer 1 for CSGNN. Default is 64.')
    parser.add_argument('--hidden2', default=32,
                        help='Number of hidden units for encoding layer 2 for CSGNN. Default is 32.')
    parser.add_argument('--hidden3', default=16,
                        help='Number of hidden units for encoding layer 3 for CSGNN. Default is 16.')
    parser.add_argument('--decoder1', default=512,
                        help='Number of hidden units for decoding layer 1 for CSGNN. Default is 512.')
    parser.add_argument('--zhongzi', default=0,
                        help='Number of zhongzi.')
    
    args = parser.parse_args()
    return args
