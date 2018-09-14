import os

def assure_path_exists(path):
    """Make sure the input path already exists.
    If it does not exists, a new directory will
    be created
    """
    mydir = os.path.join(os.getcwd(), path)
    if not os.path.exists(mydir):
        os.makedirs(mydir)


def check_obj_type(obj):
    print('type(obj) is {}'.format(type(obj)))
    if (hasattr(obj, 'shape')):
        print('obj.shape is {}'.format(obj.shape))
    if (hasattr(obj, 'size')):
        print('obj.size is {}'.format(obj.size))
    if (hasattr(obj, 'dtypes')):
        print('obj.dtypes are: \n{}'.format(obj.dtypes))
    print('\n')