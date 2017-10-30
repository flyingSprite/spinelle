
import zipfile
import os.path

""" Order 25：Zip file(s) and folder to one zip file.
1. Zip single file
2. Zip multi files
3. Zip single folder
4. Zip multi folders
"""


class ZipUnzipFiles(object):

    @staticmethod
    def zip(filename, dst_filename, mode='w'):
        """ To zip one file
        
        arcname: if dst_filename = 'test/xx.txt'
            If zipf.write(dst_filename), will get zip file is:
            test.zip
                +-- test/xx.txt
            this is not we want
            So, use zipf.write(dst_filename, arcname=os.path.basename(dst_filename)). will get zip file is:
            test.zip
                +-- xx.txt
            this is we want
        
        :param filename: 
        :param dst_filename: 
        :param mode: ZipFile requires mode 'r', 'w', 'x', or 'a'
        :return: 
        """
        with zipfile.ZipFile(filename, mode, zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(dst_filename, arcname=os.path.basename(dst_filename))
            zipf.close()

    @staticmethod
    def zip_folder(filename, dst_folder, mode='w'):
        with zipfile.ZipFile(filename, mode, zipfile.ZIP_DEFLATED) as zipf:
            for root_dir, sub_dirs, sub_filenames in os.walk(dst_folder):
                for sub_file in sub_filenames:
                    zipf.write(
                        os.path.join(root_dir, sub_file),
                        os.path.join(root_dir, sub_file).replace(dst_folder + os.sep, '')
                    )

    @staticmethod
    def test():
        # Zip a single file
        ZipUnzipFiles.zip(
            filename='D:/test/test_file.zip',
            dst_filename='D:/test/xx.txt',
            mode='w'
        )

        # Zip one folder
        ZipUnzipFiles.zip_folder(
            filename='D:/test/test_folder.zip',
            dst_folder='D:/test/ifolder',
            mode='w'
        )


class TarUntarFiles(object):

    @staticmethod
    def tar(filename, dst_filename, mode='w'):
        pass

# ZipUnzipFiles.test()
