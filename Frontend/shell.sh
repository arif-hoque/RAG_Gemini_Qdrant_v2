#!/bin/sh
nvm install 18
nvm use 18
npm run dev -- --host 0.0.0.0 --port 5673
exec "$@"
