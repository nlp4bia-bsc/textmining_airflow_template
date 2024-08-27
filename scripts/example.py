from airflow.decorators import task

# @task(map_index_template="{{ argument }}") This line is for add differents index in parallel execution
@task
def example_function(arguments):
    print(f"Arguments: {arguments}")
    return arguments

