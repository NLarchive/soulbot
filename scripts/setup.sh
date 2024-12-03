#!/bin/bash

set -e

echo "Setting up project environment..."

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv .venv

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
  echo "Creating .env file..."
  echo "API_KEY=YOUR_API_KEY" > .env
  echo "Please replace 'YOUR_API_KEY' in .env with your actual API key."
fi

echo "Project setup complete."