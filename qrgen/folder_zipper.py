import os
import shutil


class FolderZipper:

    @staticmethod
    def folder_to_zip(folder_path, output_filename):
        return shutil.make_archive(output_filename, 'zip', folder_path)
