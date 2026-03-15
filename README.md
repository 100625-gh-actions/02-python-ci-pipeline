# 02 - Python CI Pipeline

## What This Demonstrates

A complete CI (Continuous Integration) pipeline for a Python application. Every time code is pushed or a pull request is opened, the pipeline automatically runs the test suite.

## How It Works

```
Developer pushes code
        |
        v
GitHub Actions triggers
        |
        v
  +------------------+
  |  Checkout code   |
  +------------------+
        |
        v
  +------------------+
  |  Setup Python    |
  +------------------+
        |
        v
  +------------------+
  | Install deps     |
  +------------------+
        |
        v
  +------------------+
  |  Run pytest      |  --> Pass = green check, Fail = red X
  +------------------+
```

## Key Concepts

| Concept | What It Means |
|---------|---------------|
| `on: push` + `on: pull_request` | Multiple event triggers |
| `branches: [main]` | Only trigger for the main branch |
| `actions/checkout@v4` | Clone the repo onto the runner |
| `actions/setup-python@v5` | Install a specific Python version |
| `pip install -r requirements.txt` | Install dependencies |
| `pytest --verbose` | Run the test suite |

## File Structure

```
.github/
  workflows/
    ci.yml              <-- The CI workflow
app.py                  <-- Simple calculator module
test_app.py             <-- pytest tests for the calculator
requirements.txt        <-- Python dependencies (just pytest)
README.md               <-- This file
```

## Try It Yourself

1. Create a new GitHub repository
2. Copy these files into it
3. Push to GitHub
4. Open a pull request -- watch the CI run automatically
5. Try making a test fail and push again to see the red X
