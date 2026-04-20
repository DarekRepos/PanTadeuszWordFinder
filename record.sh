#!/usr/bin/env bash
set -euo pipefail

IMAGE_NAME="wordcounter-recorder"
OUTPUT_DIR="${PWD}/recordings"

mkdir -p "${OUTPUT_DIR}"

echo "Building Docker image: ${IMAGE_NAME}"
docker build -f Dockerfile.record -t "${IMAGE_NAME}" .

echo "Recording demo and generating GIF..."
docker run --rm \
  -v "${OUTPUT_DIR}:/output" \
  "${IMAGE_NAME}"

echo
echo "Done. Files exported to:"
echo " - ${OUTPUT_DIR}/word_counter_demo.cast"
echo " - ${OUTPUT_DIR}/word_counter_demo.gif"
