#!/usr/bin/env bash

set -e

# Applying migrations
alembic upgrade head

exec "$@"
