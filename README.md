# Docker Practice: Iris Classifier

A small project for learning Docker fundamentals: containerizing a Python machine learning script, running it reproducibly, and persisting output using volumes.

## What this does

Trains a Random Forest classifier on the classic Iris dataset using scikit-learn, evaluates it on a held-out test set, and saves the trained model to disk.

## Project structure

```
docker-practice/
├── Dockerfile          # Defines the container environment
├── requirements.txt    # Python dependencies
├── train.py             # Training script
├── .dockerignore        # Files excluded from the Docker build context
└── .gitignore            # Files excluded from git
```

## Requirements

- [Docker Desktop](https://www.docker.com/products/docker-desktop) installed and running

## Usage

**1. Build the image**

```bash
docker build -t iris-trainer .
```

**2. Run the container**

To just run it and see the output:

```bash
docker run iris-trainer
```

To persist the trained model to your local machine, mount a volume:

```bash
mkdir -p output
docker run -v $(pwd)/output:/app/output iris-trainer
```

The trained model will then be saved to `output/model.pkl` on your host machine.

## Expected output

```
Loading data...
Training model...
Test accuracy: 1.0000
Model saved to /app/output/model.pkl
```

## What this project demonstrates

- Writing a Dockerfile with a Python base image
- Installing dependencies inside a container via `requirements.txt`
- Building and running containers with `docker build` and `docker run`
- Using `.dockerignore` to keep the build context clean
- Persisting container output to the host filesystem with volume mounts (`-v`)
