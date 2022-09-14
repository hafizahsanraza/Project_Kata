import os


def get_config_from_env(name, optional=False, default=None):
    try:
        return os.environ[name]
    except KeyError as e:
        if default is not None:
            return default
        elif optional is True:
            return None
        else:
            raise ValueError(f"Missing environment configuration value for {name}") from e


def get_api_base_path():
    return "/api/v1"