import os
from include.builders.main_builder import MainDagBuilder  # type: ignore

dag_builder = MainDagBuilder(__file__)

if dag_builder.is_deployable():
    dag = dag_builder.create_dag()

    is_dev_environment = (
        os.getenv("TARGET_DAG_ENVIRONMENT") == "dev"
    )

    with dag:
        run_queries_ba = dag_builder.create_trigger_dag_run_operator(
            task_id="run_queries_ba",
            trigger_dag_id="sample_sample_queries_ba",
        )

        run_exec_dataproc = dag_builder.create_trigger_dag_run_operator(
            task_id="run_exec_dataproc",
            trigger_dag_id="sample_sample_exec_dataproc",
        )

        run_queries_ba >> run_exec_dataproc
