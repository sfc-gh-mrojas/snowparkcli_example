import os
import yaml

def project_variables(filename: str):
    import snowpark_project
    #files = os.listdir(os.path.dirname(snowpark_project.__file__))
    #return os.path.join(os.path.dirname(snowpark_project.__file__), filename)
    yaml_data = load_data_from_package(snowpark_project, filename)
    yaml_content = yaml.safe_load(yaml_data)
    return yaml_content


def load_data_from_package(package, filename):
    try:
        # Attempt to construct the file path directly
        data_path = os.path.join(os.path.dirname(package.__file__), filename)
        with open(data_path, 'rt') as file:
            return file.read()
    except:
        # __file__ is not set or path doesn't exist, use the loader
        if hasattr(package, '__loader__'):
            return package.__loader__.get_data(filename).decode('utf-8')
        else:
            raise Exception(f"Failed to load data from {filename}")
