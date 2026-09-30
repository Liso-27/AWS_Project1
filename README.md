# AWS Project 1: Dockerized App on EC2, Nginx, HTTPS, Rate Limiting, Monitoring

A web app deployed on a single AWS EC2 instance. Containerized with Docker, served through Nginx with a free TLS certificate, protected by rate limiting, and watched by a CloudWatch alarm.

Live demo: https://soumyapasswordapp.duckdns.org

The instance is stopped when it's not being actively demoed, to stay within AWS free tier. Redeploying takes under 5 minutes, steps are below.

## Architecture
-> soumyapasswordapp.duckdns.org (free dynamic DNS)
-> EC2 instance, port 443
-> Nginx (TLS termination, reverse proxy, rate limiting)
-> Docker container, port 5000
-> Gunicorn, 3 workers


## Problems found and fixed

### 1. One request at a time

The app's default server could only handle one request at a time. Everything else waited in line. Switched to Gunicorn with 3 worker processes and load tested both versions with Apache Bench (`ab -n 200 -c 20`).

| | Requests/sec | Avg response time |
|---|---|---|
| Before | 523.52 | 38.2 ms |
| After | 1236.58 | 16.17 ms |

2.4x more throughput, 58% faster, no failed requests either way.

Proof: `docs/proof/gunicorn-before.png`, `docs/proof/gunicorn-after.png`

### 2. No limit on requests to a public endpoint

Anyone could send unlimited requests to the app's API endpoint. Added Nginx rate limiting, 5 requests per second per IP, with a burst allowance of 10. Tested by firing 100 requests at once (`ab -n 100 -c 30`).

88 of 100 got rejected with a 503. Normal browsing wasn't affected.

Proof: `docs/proof/rate-limit-test.png`

### 3. No way to know if the server died

Set up a CloudWatch alarm watching `StatusCheckFailed`, wired to an SNS topic that emails me the moment the instance stops responding.

Proof: `docs/proof/cloudwatch-alarm.png`

## Security

- SSH restricted to a single known IP, not open to the internet
- Only ports 22, 80, and 443 open
- HTTPS enforced, all HTTP traffic redirects to HTTPS
- Free certificate via Let's Encrypt / Certbot, auto-renews

## Run it yourself

```bash
git clone https://github.com/Liso-27/AWS_Project1.git
cd AWS_Project1
docker build -t password-analyzer .
docker run -d -p 5000:5000 --name password-analyzer-container password-analyzer
```

Then point Nginx at port 5000 and set up Certbot for HTTPS, or just hit port 5000 directly for local testing.

## Stack

AWS EC2, Docker, Nginx, Gunicorn, Certbot, Amazon CloudWatch, SNS, DuckDNS
