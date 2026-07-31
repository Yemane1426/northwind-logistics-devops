# Assessment Evidence Matrix

| Criterion | Implementation | Verification | Evidence |
|---|---|---|---|
| Version control | Feature branches and Pull Requests | Protected main workflow | Add PR link |
| Automated tests | Unit and real HTTP integration tests | Pytest and coverage gate | Add workflow link |
| Code quality | Flake8 | CI quality job | Add workflow link |
| Python security | Bandit | Security workflow | Add workflow link |
| Dependency security | pip-audit and dependency review | CI and PR checks | Add workflow link |
| Containerisation | Hardened non-root Docker image | Health and user checks | Add workflow link |
| Image security | Trivy container scan | Security workflow | Add workflow link |
| Kubernetes | Deployment, Service, probes and resources | Kind and Minikube | Add workflow link |
| Kubernetes security | Non-root, seccomp, dropped capabilities and NetworkPolicy | Manifest validation | Add evidence link |
| Reliability | Two replicas, rolling update, rollback and PDB | Rollout tests | Add evidence link |
| Configuration management | Ansible playbook | Syntax and idempotency checks | Add evidence link |
| CI/CD | Test, build, deployment verification and publication | GitHub Actions | Add workflow link |
| Registry | GHCR latest and SHA images | Package publication | Add package link |
| Documentation | README, evidence matrix and limitations | Repository review | Add repository link |