#!/usr/bin/env bash
set -e

args=($@)
echo "Running with $@"

# Loads environment variables, if exists
if [ -f "/etc/application-env/common.sh" ]; then
  source /etc/application-env/common.sh
fi

exec gunicorn -w 4 -b 0.0.0.0:5000 project.app:app
