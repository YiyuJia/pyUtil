import h5py


def save_file(data, filename, dataset_name='data'):
    """Save a np.array.
    Args:
        data (np.array): An array.
        filename (str): Name of the file.
    Examples:
        >>> import numpy as np
        >>> a = np.array([[1,2,3],[4,5,6]])
        >>> save_file(a, 'file.hdf5')

    """
    with h5py.File(filename, 'w') as f:
        f[dataset_name] = data


def read_file(filename, dataset_name='data'):
    """Read a hdf5 file.
    Args:
        filename (str): Name of the file.
    Returns:
        data (np.array): An array.
    Examples:
        >>> b = read_file('file.hdf5')
        >>> b
        array([[1, 2, 3],
               [4, 5, 6]])


    """
    with h5py.File(filename, 'r') as f:
        X = f[dataset_name][...]
    return X
