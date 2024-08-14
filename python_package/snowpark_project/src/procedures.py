from snowflake.snowpark import Session

from snowpark_project.src.common import project_variables
def hello_procedure(session: Session) -> str:
    return f"{project_variables('snowpark_project/project.yml')}"
