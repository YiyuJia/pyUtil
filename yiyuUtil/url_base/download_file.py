import sys
import os
import wget
if sys.version_info.major == 2:
    # Backward compatibility with python 2.
    from six.moves import urllib
    urlretrieve = urllib.request.urlretrieve
else:
    from urllib.request import urlretrieve


def maybe_download(work_directory, filename, url, expected_bytes=None, verbose=False):
    """Download a file if it is not already downloaded.
    Args:
        work_directory (str): Path name without file name
        filename (str): File name without path name.
        url (str): URL of the file to download.
        expected_bytes (int): Expected file size in bytes.
        verbose (bool): Verbose flag
    Returns:
        filename (str): File name of the file downloaded
    Examples:
        >>> url = 'https://raw.githubusercontent.com/miguelgfierro/codebase/master/LICENSE'
        >>> if os.path.exists('license.txt'): os.remove('license.txt')
        >>> filename = maybe_download('license.txt', url, expected_bytes=1531, verbose=True)
        File license.txt verified with 1531 bytes
        >>> filename = maybe_download('license.txt', url, expected_bytes=1531, verbose=True)
        File license.txt already downloaded
        File license.txt verified with 1531 bytes
        >>> filename = maybe_download('license.txt', url)
        >>> filename
        'license.txt'

    """
    if not os.path.exists(work_directory):
        os.mkdir(work_directory)
    filepath = os.path.join(work_directory,filename)
    if not os.path.exists(filepath):
        if verbose:
            filepath = wget.download(url, out=filepath)
        else:
            filepath, _ = urlretrieve(url, filepath)
    else:
        if verbose: print("File {} already downloaded".format(filepath))
    if expected_bytes is not None:
        statinfo = os.stat(filepath)
        if statinfo.st_size == expected_bytes:
            if verbose: print('File {} verified with {} bytes'.format(filepath, expected_bytes))
        else:
            raise Exception('Failed to verify {}'.format(filepath))
    return filepath


