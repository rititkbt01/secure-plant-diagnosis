# BACKEND - FastAPI Secure Server

## Purpose
REST API connecting mobile app → AI model → remedies:
- /predict          - Disease diagnosis (JWT protected)
- /remedy           - Treatment lookup  
- /health           - Server status

## Tech Stack
- FastAPI (async Python)
- PostgreSQL (remedy database)
- JWT Authentication
- TLS 1.3 Encryption
- Rate limiting + input validation

## Security Features
1. Magic byte image validation
2. SQL injection prevention  
3. DoS protection (10 req/min)
4. OWASP Top 10 compliance

## Status: Ritik Budhathoki (Security Lead)
