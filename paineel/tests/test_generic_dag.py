import os
from textwrap import dedent


def test_generic_dag(monkeypatch, tmp_path):
    yaml_content = dedent(
        """
        dag:
          id: sample-dag
          schedule: "0 0 * * *"
          owner: ["tester"]
          commands:
            - task_id: say_hello
              type: bash
              script: echo
              args: ["hello"]
        """
    )
    config_file = tmp_path / "pa_sample.yaml"
    config_file.write_text(yaml_content)
    monkeypatch.setenv("PA_DAG_CONF_DIR", str(tmp_path))

    from dags.paineel_src.parsers import YAMLParser
    specs = YAMLParser(str(config_file)).parse()

    from dags.paineel_src.dou_dag_generator import DouDigestDagGenerator
    generator = DouDigestDagGenerator()
    dag = generator.create_generic_dag(specs)

    assert dag.dag_id == "pa_sample-dag"
    assert len(dag.tasks) == 1
    task = dag.tasks[0]
    assert task.task_id == "pa_say_hello"
    assert task.bash_command.strip() == "echo hello"
