from pathlib import Path

# Allow importing modules from the PAINEEL source directory as a subpackage of
# ``dags`` so that tests can resolve ``dags.paineel_src``.
__path__.append(str(Path(__file__).resolve().parents[2] / 'paineel' / 'src'))
