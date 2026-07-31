# Contributing

## Workflow

1. Create a feature branch from `main`.
2. Make one focused change.
3. Run all local quality checks.
4. Commit with a clear message.
5. Push the feature branch.
6. Open a Pull Request.
7. Merge only after all required checks pass.

## Required local checks

```text
python -m flake8 app tests --max-line-length=100
python -m bandit -r app -ll
python -m pip_audit -r requirements-dev-lock.txt
python -m pytest --cov=app --cov-branch --cov-fail-under=90
docker build -t northwind-logistics:test .
kubectl apply --dry-run=client -f k8s/
```