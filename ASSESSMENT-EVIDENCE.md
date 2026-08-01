# Assessment Evidence Matrix

| Criterion | Implementation | Verification | Evidence |
|---|---|---|---|
| Version control | Feature branches and Pull Requests | Protected `main` workflow and required checks | [Main improvement PR #17](https://github.com/Yemane1426/northwind-logistics-devops/pull/17) |
| Automated tests | Unit tests and real HTTP integration tests | Pytest with line and branch coverage gate | [CI/CD successful run](https://github.com/Yemane1426/northwind-logistics-devops/actions/runs/30673960204) |
| Code quality | Flake8 and Python compilation | CI Quality and Tests job | [CI/CD successful run](https://github.com/Yemane1426/northwind-logistics-devops/actions/runs/30673960204) |
| Python security | Bandit static analysis | Python Security job | [Security successful run](https://github.com/Yemane1426/northwind-logistics-devops/actions/runs/30673960207) |
| Dependency security | pip-audit, Dependency Review and Dependabot | CI and Pull Request security checks | [Dependency Review successful run](https://github.com/Yemane1426/northwind-logistics-devops/actions/runs/30673798251) |
| Containerisation | Hardened non-root Docker image with health check | Docker build, health endpoint and UID verification | [Dockerfile](https://github.com/Yemane1426/northwind-logistics-devops/blob/main/Dockerfile) |
| Image security | Trivy container-image vulnerability scan | Container Image Scan job | [Security successful run](https://github.com/Yemane1426/northwind-logistics-devops/actions/runs/30673960207) |
| Kubernetes | Deployment, Service, probes and resource controls | CI Kubernetes deployment and Minikube testing | [CI/CD successful run](https://github.com/Yemane1426/northwind-logistics-devops/actions/runs/30673960204) |
| Kubernetes security | Non-root user, seccomp, read-only filesystem, dropped capabilities and NetworkPolicy | Manifest validation and runtime UID verification | [Production Deployment](https://github.com/Yemane1426/northwind-logistics-devops/blob/main/k8s/production/deployment.yaml), [NetworkPolicy](https://github.com/Yemane1426/northwind-logistics-devops/blob/main/k8s/network-policy.yaml) |
| Reliability | Two replicas, rolling updates, health probes and PodDisruptionBudget | Kubernetes rollout and ready-replica verification | [PodDisruptionBudget](https://github.com/Yemane1426/northwind-logistics-devops/blob/main/k8s/pod-disruption-budget.yaml) |
| Configuration management | Ansible playbook | Syntax validation and idempotency verification | [Ansible configuration](https://github.com/Yemane1426/northwind-logistics-devops/tree/main/ansible) |
| CI/CD | Tests, container build, Kubernetes verification and image publication | Required GitHub Actions checks | [CI/CD successful run](https://github.com/Yemane1426/northwind-logistics-devops/actions/runs/30673960204) |
| Registry | GHCR `latest` and commit-SHA images | Package publication and image pull test | [GHCR package](https://github.com/Yemane1426/northwind-logistics-devops/pkgs/container/northwind-logistics) |
| Documentation | README, security policy, contribution guide, evidence matrix and limitations | Repository review | [README](https://github.com/Yemane1426/northwind-logistics-devops/blob/main/README.md) |

## Key submission references

- Repository: [Northwind Logistics DevOps](https://github.com/Yemane1426/northwind-logistics-devops)
- Main implementation Pull Request: [PR #17](https://github.com/Yemane1426/northwind-logistics-devops/pull/17)
- Submission-information Pull Request: [PR #25](https://github.com/Yemane1426/northwind-logistics-devops/pull/25)
- README update Pull Request: [PR #26](https://github.com/Yemane1426/northwind-logistics-devops/pull/26)
- CI/CD successful run: [GitHub Actions run 30673960204](https://github.com/Yemane1426/northwind-logistics-devops/actions/runs/30673960204)
- Security successful run: [GitHub Actions run 30673960207](https://github.com/Yemane1426/northwind-logistics-devops/actions/runs/30673960207)
- Dependency Review successful run: [GitHub Actions run 30673798251](https://github.com/Yemane1426/northwind-logistics-devops/actions/runs/30673798251)
- Release Validation successful run: [GitHub Actions run 30672382615](https://github.com/Yemane1426/northwind-logistics-devops/actions/runs/30672382615)
- GHCR package: [northwind-logistics](https://github.com/Yemane1426/northwind-logistics-devops/pkgs/container/northwind-logistics)
- Release tag: [`v1.0.0`](https://github.com/Yemane1426/northwind-logistics-devops/releases/tag/v1.0.0)