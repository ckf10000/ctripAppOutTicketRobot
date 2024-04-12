# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  ctripAppOutTicketRobot
# FileName:     dir.py
# Description:  TODO
# Author:       GIGABYTE
# CreateDate:   2024/04/12
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
import os
import typing as t


def get_project_path():
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


def get_images_dir():
    return os.path.join(get_project_path(), "static", "images")


def is_exists(file_name: t.LiteralString | str | bytes) -> bool:
    if os.path.exists(file_name):
        return True
    else:
        return False


def is_file(file_path: str):
    if os.path.isfile(file_path):
        return True
    else:
        return False


def is_dir(file_path: str):
    if os.path.isdir(file_path):
        return True
    else:
        return False


def join_path(path_slice: list) -> t.LiteralString | str | bytes:
    return os.path.join(*path_slice)


if __name__ == "__main__":
    print(get_project_path())
