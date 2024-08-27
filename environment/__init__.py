import yaml

env_file = 'dags/textmining_airflow_template/environment/application-prod.yml'

def read_yaml(file_path):
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as exc:
            print(f"Error reading YAML file: {exc}")
            return None

env = read_yaml(env_file)