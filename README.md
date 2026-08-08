# Northwind Logistics Delivery Tracking Service
## Submission Information

Submission evidence baseline commit: `59ebdd45b7b8b6f981cd17ca646ed667914b0f97`

## 1. Project scope

This project implements a Python-based REST API for tracking Northwind Logistics deliveries while demonstrating a complete DevOps workflow. The project includes automated testing, containerisation, Kubernetes deployment, Ansible environment automation, GitHub Actions CI/CD, and GitHub Container Registry (GHCR) image publication.

---

## 2. Application endpoints

| Endpoint | Description |
|----------|-------------|
| GET / | Service information |
| GET /health | Health check endpoint |
| GET /deliveries | Returns all deliveries |
| GET /deliveries/{id} | Returns a single delivery |
---

## 3. DevOps architecture

```
                GitHub Repository
                       │
             Pull Request Workflow
                       │
             GitHub Actions CI/CD
      ┌───────────────┼────────────────┐
      │               │                │
 Quality & Tests   Docker Build   Kubernetes (kind)
      │               │                │
      └───────────────┼────────────────┘
                      │
                Publish Image
                  to GHCR
                      │
               Production-ready Image
```

---

## 4. Repository structure

```
app/
tests/
k8s/
ansible/
screenshots/
.github/workflows/
Dockerfile
README.md
requirements.txt
run.py
```

---

## 5. Technology choices and rationale

| Technology | Purpose |
|------------|---------|
| Python | REST application |
| Pytest | Automated testing |
| Flake8 | Code quality |
| Docker | Containerisation |
| Kubernetes | Container orchestration |
| Minikube | Local Kubernetes cluster |
| Kind | Temporary CI Kubernetes cluster |
| GitHub Actions | Continuous Integration / Deployment |
| GHCR | Container image registry |
| Ansible | Environment automation |

---

## 6. Local Python setup

Create and activate a virtual environment.

Windows

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Run the application:

```powershell
python run.py
```

---

## 7. Automated testing

Run all tests:

```powershell
pytest
```

Run coverage:

```powershell
python -m pytest --cov=app --cov-branch --cov-report=term-missing --cov-fail-under=90
```

---

## 8. Docker build and execution

Build:

```powershell
docker build -t northwind-logistics:test .
```

Run:

```powershell
docker run -p 8000:8000 northwind-logistics:test
```

Health check:

```
http://localhost:8000/health
```

---

## 9. Kubernetes deployment with Minikube

Apply manifests:

```powershell
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Verify:

```powershell
kubectl get deployments
kubectl get pods
kubectl get services
```

---

## 10. Ansible environment configuration

Syntax check:

```bash
ansible-playbook -i ansible/inventory.ini ansible/playbook.yml --syntax-check
```

Run playbook:

```bash
ansible-playbook -i ansible/inventory.ini ansible/playbook.yml --ask-become-pass
```

The playbook creates a persistent Linux virtual environment, installs dependencies, and verifies the application.

---

## 11. CI/CD pipeline

The GitHub Actions pipeline performs:

- Code linting
- Automated testing
- Coverage verification (100%)
- Docker build
- Container smoke testing
- Kubernetes deployment using Kind
- Kubernetes rollout verification
- Health endpoint verification
- GHCR publication after merging to main
 CI/CD pipeline verification completed.
---

## 12. Image publication

After merging into the main branch, GitHub Actions automatically publishes the Docker image to GitHub Container Registry (GHCR).

Published tags include:

- latest
- Commit SHA

---

## 13. Evidence index

| Evidence | What it demonstrates |
|---|---|
| Pull Request history | Reviewable feature-branch workflow |
| HTTP test success | Automated service-level testing |
| Failed-test demonstration | Tests fail clearly when behaviour is wrong |
| Coverage output | Enforced test coverage quality gate |
| Non-root container | Improved container security |
| Container health output | Runtime health-check support |
| Kubernetes deployment | Working Deployment and Service |
| Scaling evidence | Horizontal replica scaling |
| Rolling update | Controlled application update |
| Rollback evidence | Deployment recovery capability |
| Ansible first run | Automated environment setup |
| Ansible second run | Idempotent behaviour |
| CI Kubernetes job | Real deployment in a temporary cluster |
| Health-check job | Deployed application is reachable |
| GHCR package | Deployment-ready image publication |

---

## 14. Security and reliability measures

The project includes several reliability and security improvements:

- Non-root Docker container execution
- Docker health checks
- Automated linting
- Automated testing
- Coverage enforcement
- Kubernetes readiness verification
- Rolling updates
- Rollback capability
- Temporary Kubernetes deployment verification during CI
- Automated container publication to GHCR

---

## 15. Limitations

- The local Minikube cluster is single-node and does not demonstrate multi-node high availability.
- Application data is held in memory and is lost when containers restart.
- The CI Kubernetes cluster is temporary and used for deployment verification, not production hosting.
- NodePort is suitable for local demonstration, while production systems would normally use an Ingress or managed load balancer.
- The project does not include persistent storage, monitoring, a database, or secrets management.

---

## 16. Future improvements

Potential future enhancements include:

- PostgreSQL integration
- Persistent Kubernetes storage
- Helm charts
- Prometheus monitoring
- Grafana dashboards
- Kubernetes Ingress
- TLS certificates
- Secrets management
- Multi-node Kubernetes deployment
- Continuous deployment to a cloud Kubernetes cluster

## Security checks

Run Python static security analysis:

```bash
python -m bandit -r app -ll
```

Audit locked development dependencies:

```bash
python -m pip_audit -r requirements-dev-lock.txt
```

The CI pipeline also scans repository files, infrastructure configuration and
the container image for high and critical findings.

## Kubernetes environments

The `k8s/` manifests use a locally loaded Docker image for Minikube and Kind.

The `k8s/production/` manifests demonstrate registry-based deployment using
the image published to GitHub Container Registry. An immutable commit-SHA
image should be used for an actual production release.