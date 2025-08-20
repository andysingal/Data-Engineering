This MCP server performs the following:

- Finds Dockerfiles in your repo.
- Builds Docker images from them.
- Scans for vulnerabilities using Trivy.
- Applies patches using Copacetic (optional)*
- Re-scans to verify fixes.
- Optionally updates your Dockerfile with security fixes.

[container-security-mcp](https://github.com/anishgupta19/container-security-mcp/tree/main)

Docker security scanner with automated vulnerability patching via Trivy + Copacetic.
