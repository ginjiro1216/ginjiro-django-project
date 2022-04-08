set -eux

python -m isort .

python -m autoflake . \
  -i \
  -r \
  --ignore-init-module-imports \
  --remove-all-unused-imports \
  --remove-duplicate-keys \
  --remove-unused-variables \
  --exclude venv

python -m black . --exclude venv
