from pathlib import Path

# Allow importing modules from the ro-dou source directory as a subpackage of
# ``dags`` so that tests can resolve ``dags.ro_dou_src``.
__path__.append(str(Path(__file__).resolve().parents[2] / 'ro-dou' / 'src'))
