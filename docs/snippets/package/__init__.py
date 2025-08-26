from importlib import metadata

def get_version(dist: str = "mkdocstrings-python") -> str:
    """Get version of the given distribution.

    Parameters:
        dist: A distribution name.

    Returns:
        A version number.
    """
    try:
        return metadata.version(dist)
    except metadata.PackageNotFoundError:
        return "0.0.0"


current_version: str = get_version(dist="mkdocstrings-python")
"""Current package version."""
