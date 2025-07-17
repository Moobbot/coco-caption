__author__ = 'tylin'
import os
import sys

# Thêm thư mục gốc của pycocoevalcap vào sys.path nếu chưa có
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)