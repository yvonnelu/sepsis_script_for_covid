import os
import pickle


def save_pickle(obj, filename, protocol=4, create_folder=True):
    """Basic pickle/dill dumping.

    Given a python object and a filename, the method will save the object under that filename.

    Args:
        obj (python object): The object to be saved.
        filename (str): Location to save the file.
        protocol (int): Pickling protocol (see pickle docs).
        create_folder (bool): Set True to create the folder if it does not already exist.

    Returns:
        None
    """
    if create_folder:
        _create_folder_if_not_exist(filename)

    # Save
    with open(filename, 'wb') as file:
        pickle.dump(obj, file, protocol=protocol)


def load_pickle(filename):
    """Basic pickle load function.

    Args:
        filename (str): Location of the object.

    Returns:
        python object: The loaded object.
    """
    with open(filename, 'rb') as file:
        obj = pickle.load(file)
    return obj


def _create_folder_if_not_exist(filename):
    """ Makes a folder if the folder component of the filename does not already exist. """
    os.makedirs(os.path.dirname(filename), exist_ok=True)


