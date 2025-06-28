# gRPC GitHub Repo Access Checker

This project provides a gRPC-based service that checks which GitHub repositories a given user can access based on Open Policy Agent (OPA) authorization policies.

---

## ⚙️ Requirements

- **Python**: 3.10.18
- **OPA (Open Policy Agent)**: Tested with **v0.63.0**

📦 Install Python dependencies:

```bash
pip install -r requirements.txt
```

📥 Download OPA from the official site:  
[https://www.openpolicyagent.org/docs?current-os=windows#1-download-opa](https://www.openpolicyagent.org/docs?current-os=windows#1-download-opa)

Place `opa.exe` somewhere accessible via your system PATH.

---

## 🔑 GitHub Token Setup

To connect to the GitHub API as an admin:

1. Go to [https://github.com/settings/tokens](https://github.com/settings/tokens)
2. Create a **classic token**
3. Enable at minimum the **`repo` scope** (full access to repositories)
4. Save the token and org name in a `.env` file in your project root:

```env
GITHUB_TOKEN=ghp_your_generated_token_here
ORG_NAME=your_org_name
```

Make sure this matches the exact name of your GitHub organization (not a username).

---

## 🚀 How to Run the System

### 1️⃣ Start the OPA Server

From the project root, run:

```bash
opa run --server --watch opa_auth/authz.rego
```

OPA will load policy from `opa_auth/authz.rego`.

> 🔧 You can configure access logic in `authz.rego`. This file defines who has access based on their permissions.

---

### 2️⃣ Start the gRPC Server

In a new terminal:

```bash
python -m grpc_server.grpc_server
```

This service will use your GitHub token to fetch repo access and evaluate it using OPA.

---

### 3️⃣ Run the gRPC Client

In another terminal:

```bash
python grpc_client.py <github-username>
```
