#!/bin/bash

# Install Python dependencies
pip install -r requirements.txt

# Build frontend
cd frontend
npm install
npm run build