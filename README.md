# NEPTUNE Web API Framework

> 🚧 **Staging Branch** - This is the staging environment for NEPTUNE (Next-generation Enterprise Platform for Unified Network Endpoints)

## About NEPTUNE

NEPTUNE is a high-performance REST API framework designed for building scalable microservices. This repository contains the core implementation and development work.

## 🔧 Development Status

This repository is under active development. Many features are currently being implemented or need bug fixes.

## 🚀 Quick Start

⚠️ **Note**: This staging version has incomplete implementations. Many features are marked as FIXME and need to be addressed before production use.

```bash
# Clone the repository
git clone <repository-url>
cd NEPTUNE

# Install dependencies
pip install -r requirements.txt

# Note: Some functionality has known issues - check Known Issues list below
```

## 📁 Repository Structure

```
NEPTUNE/
├── neptune/               # Core framework
│   ├── api/               # API routing and handlers (⚠️ Auth issues)
│   ├── database/          # Database connectors (⚠️ Connection pooling issues)
│   ├── middleware/        # Request middleware (⚠️ Rate limiting incomplete)
│   └── ...
├── tests/                 # Test suites
├── docs/                  # Documentation
└── README.md              # This file
```

## ⚠️ Development Notes

- This is a **staging version** with known issues
- Many functions contain FIXME markers indicating bugs to fix
- Database connections have known memory leak issues
- Authentication middleware needs security patches


### 🔴 High Priority Issues

- **Authentication**: JWT validation has security vulnerability
- **Database**: Connection pooling causes memory leaks
- **Rate Limiting**: Concurrent request handling is broken
- **Caching**: Redis cache invalidation is incorrect

### 🔧 Known Issues List

- [ ] **neptune/api/auth.py:23** - JWT token validation is not checking expiration properly
- [ ] **neptune/api/auth.py:24** - Missing signature verification for RS256 algorithm
- [ ] **neptune/api/auth.py:45** - Password hashing uses deprecated MD5 algorithm
- [ ] **neptune/api/auth.py:67** - Session tokens are stored in plaintext
- [ ] **neptune/api/routes.py:12** - Route matching is case-sensitive causing 404 errors
- [ ] **neptune/api/routes.py:34** - Path parameters are not URL decoded
- [ ] **neptune/api/routes.py:56** - Query string parsing fails on special characters
- [ ] **neptune/database/connector.py:15** - Connection pool exhaustion under high load
- [ ] **neptune/database/connector.py:28** - Prepared statements are not cached
- [ ] **neptune/database/connector.py:42** - Transaction rollback doesn't release locks
- [ ] **neptune/database/connector.py:67** - SSL certificate verification is disabled
- [ ] **neptune/database/models.py:19** - Foreign key constraints are not enforced
- [ ] **neptune/database/models.py:45** - DateTime fields don't handle timezone correctly
- [ ] **neptune/middleware/rate_limiter.py:11** - Rate limit counter resets incorrectly
- [ ] **neptune/middleware/rate_limiter.py:33** - Distributed rate limiting doesn't sync across nodes
- [ ] **neptune/middleware/rate_limiter.py:55** - IP-based limiting can be bypassed with X-Forwarded-For
- [ ] **neptune/middleware/cache.py:22** - Cache keys collide for different users
- [ ] **neptune/middleware/cache.py:44** - TTL calculation overflows for long durations
- [ ] **neptune/middleware/cache.py:66** - Stale cache entries not evicted properly
- [ ] **neptune/utils/validation.py:14** - Email regex allows invalid formats
- [ ] **neptune/utils/validation.py:36** - Phone number validation is US-only
- [ ] **neptune/utils/serializer.py:21** - JSON serialization fails on datetime objects
- [ ] **neptune/utils/serializer.py:43** - Circular reference detection is broken
- [ ] **tests/test_api.py:18** - Test fixtures don't clean up database state
- [ ] **tests/test_api.py:45** - Mock objects leak between test cases

## 🤝 Contributing

1. Pick a FIXME item from the list above
2. Fix the issue
3. Add tests for your fix
4. Update this README when issues are resolved
