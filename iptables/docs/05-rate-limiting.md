# Rate Limiting

## Purpose
Implements rate limiting to protect network services
from brute-force attacks and basic denial-of-service
attempts.

## What Is Rate Limiting
Rate limiting restricts how frequently a client can
initiate new connections to a service within a given
time window.

## Rules Applied
- Limit new SSH connections to 3 per minute per source IP
- Drop excess connection attempts

## Why SSH Is Protected
SSH is a common target for:
- Brute-force password attacks
- Credential stuffing
- Automated scanning

Limiting connection attempts significantly reduces
attack effectiveness.

## Security Benefits
- Reduces attack surface
- Slows automated attacks
- Preserves system availability

## Limitations
- Not a full DoS mitigation solution
- Works best combined with logging and monitoring

## Execution Order
This script runs after service whitelisting and applies
additional protection to allowed services.
