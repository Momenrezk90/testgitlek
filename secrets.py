#!/usr/bin/env python3
"""
Test Application with Intentional Secrets
These secrets WILL be detected by GitLeaks
"""

# AWS Credentials (WILL BE DETECTED)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# GitHub Personal Access Token (WILL BE DETECTED)
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyzABC"

# Stripe API Key (WILL BE DETECTED)
STRIPE_SECRET_KEY = "sk_live_1234567890abcdefghijklmnopqrstuvwxyz"
STRIPE_PUBLISHABLE = "pk_live_1234567890abcdefghijklmnopqrstuvwxyz"

# SendGrid API Key (WILL BE DETECTED)
SENDGRID_API_KEY = "SG.1234567890abcdefghijklmnopqrstuvwxyz.1234567890abcdefghijklmnopqrstuvwxyz"

# Slack Webhook (WILL BE DETECTED)
SLACK_WEBHOOK = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"

# Database Connection String with Password (WILL BE DETECTED)
DATABASE_URL = "postgresql://admin:MySecretP@ssw0rd123!@db.example.com:5432/production_db"

# Private SSH Key (WILL BE DETECTED)
PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN
OPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR
-----END RSA PRIVATE KEY-----"""

# API Tokens
OPENAI_API_KEY = "sk-proj-1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
ANTHROPIC_API_KEY = "sk-ant-1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# JWT Secret
JWT_SECRET = "my-super-secret-jwt-key-do-not-share-123456789"

# Configuration
API_CONFIG = {
    "api_key": "AIzaSyD1234567890abcdefghijklmnopqrstuv",  # Google API Key
    "secret": "secret_key_1234567890abcdefghijklmnop"
}

def main():
    print("⚠️  This file contains intentional secrets for testing GitLeaks")
    print("🔍 GitLeaks should detect and flag all of these!")
    print(f"🔑 AWS Key: {AWS_ACCESS_KEY_ID[:10]}...")
    print(f"🔑 GitHub Token: {GITHUB_TOKEN[:10]}...")
    print(f"🔑 Stripe Key: {STRIPE_SECRET_KEY[:10]}...")

if __name__ == "__main__":
    main()
