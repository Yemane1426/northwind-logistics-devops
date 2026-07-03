# Northwind Logistics Delivery Tracking Service

## Project Overview

This repository contains a DevOps solution for the Northwind Logistics delivery-tracking Python application. The solution includes automated testing, GitHub Actions CI/CD, Ansible environment setup, Docker containerisation, and Kubernetes orchestration using Minikube.

## Architecture

Developer → GitHub → GitHub Actions → Pytest → Docker Image → Kubernetes Deployment → NodePort Service → Running Application

## Tools Used

- Git and GitHub
- Python 3.11
- Pytest and pytest-cov
- GitHub Actions
- Docker
- Kubernetes with Minikube
- Ansible

## Repository Structure

```text
app/
tests/
.github/workflows/ci-cd.yml
ansible/
k8s/
Dockerfile
README.md
requirements.txt
screenshots/