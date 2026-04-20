# Developer Guide: Terminal Recording

## Overview

This document describes the technical process used to automate terminal recordings for this project.
The goal is to provide a clean, reproducible demo workflow using `asciinema`, so visual documentation can be refreshed safely after CLI changes.

## Tools Used

- `asciinema` - records terminal sessions into `.cast` files.
- `agg` - converts `.cast` files into animated `.gif` files.
- `Docker` - isolates the recording environment from the local machine.

## Scripts Breakdown

### `record.sh` and `record_demo.sh`

- `record.sh` is the main host-side entrypoint.
- It builds the recorder image from `Dockerfile.record`, runs the container, and exports generated assets to `recordings/`.
- `record_demo.sh` is a legacy helper from an earlier stage of the setup. It can still be used for basic pipeline checks, but the current demo flow is driven by `demo_script.sh`.

### `demo_script.sh`

`demo_script.sh` is the automation script executed inside the container. It is responsible for:

- preparing deterministic input files for the demo scenario,
- running scripted CLI commands in a fixed sequence,
- simulating typed commands (to reduce manual mistakes during recording),
- producing a `.cast` recording and converting it into a `.gif`.

## Docker Isolation

`Dockerfile.record` creates a fresh, minimal recording environment so demos do not expose local WSL paths, shell history, host-specific settings, or sensitive data.

### Build image

```bash
docker build -f Dockerfile.record -t wordcounter-recorder .
```

### Run container with output volume

```bash
docker run --rm -v "$(pwd)/recordings:/output" wordcounter-recorder
```

In normal usage, both commands are already wrapped by `record.sh`.

## Recording Workflow

### 1. Build the recorder image

Use `record.sh` or run the Docker build manually:

```bash
docker build -f Dockerfile.record -t wordcounter-recorder .
```

### 2. Record terminal session to `.cast`

Inside the container, `asciinema` records the scripted session:

```bash
asciinema rec --overwrite --idle-time-limit 1 --command "bash /tmp/demo_commands.sh" /output/word_counter_demo.cast
```

### 3. Convert `.cast` to `.gif`

Conversion is handled by `agg`:

```bash
agg /output/word_counter_demo.cast /output/word_counter_demo.gif
```

## Output Location

All generated visual artifacts are written to:

- `recordings/word_counter_demo.cast`
- `recordings/word_counter_demo.gif`

## Recommended Refresh Command

For day-to-day development, refresh demo assets with:

```bash
chmod +x record.sh
./record.sh
```

This is the preferred developer workflow for updating visual documentation after CLI changes.
