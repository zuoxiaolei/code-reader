import os
import shutil
from typing import List
from magika import Magika

magika = Magika()
result = magika.identify_bytes
text_type = {'text', 'code'}


def is_ignore_path(path_name: str) -> bool:
    '''过滤特殊的目录'''
    for short_path in path_name.split(os.sep):
        if short_path.startswith("."):
            return True
    return False


def get_all_file(directory: str) -> List[str]:
    '''获取目录所有文件'''
    all_filenames = []
    for root, dirs, files in os.walk(directory):
        if not is_ignore_path(root):
            for filename in files:
                full_filename = os.path.join(root, filename)
                all_filenames.append(full_filename)
    return all_filenames


def get_file_size(file_path):
    """
    Get the size of a file in bytes.
    """
    return os.path.getsize(file_path)


def detect_file_type(filenames: List[str]) -> List[str]:
    file_type_labels = []
    for filename in filenames:
        file_size_in_mb = os.path.getsize(filename) / 1024 / 1024
        if file_size_in_mb < 1:
            with open(filename, 'rb') as fh:
                file_bytes = fh.read()
                file_type = magika.identify_bytes(file_bytes)
                file_type_labels.append(file_type.output.group)
        else:
            print(filename, file_size_in_mb)
            file_type_labels.append("unknow")
    return file_type_labels


def get_text_file(directory: str) -> List[str]:
    all_filenames = get_all_file(directory)
    file_type_labels = detect_file_type(all_filenames)
    filter_filenames = []
    for filename, file_type in zip(all_filenames, file_type_labels):
        if file_type in text_type:
            filter_filenames.append(filename, file_type)
    return filter_filenames


if __name__ == '__main__':
    from pprint import pprint
    all_filenames = get_text_file("/Users/xiaoleizuo/workspace/TextRankPlus")
    print(all_filenames)