#!/usr/bin/env bash
set -euo pipefail

OUTPUT_DIR="${OUTPUT_DIR:-/output}"
CAST_FILE="${OUTPUT_DIR}/word_counter_demo.cast"
GIF_FILE="${OUTPUT_DIR}/word_counter_demo.gif"
DEMO_COMMANDS_FILE="/tmp/demo_commands.sh"

mkdir -p "${OUTPUT_DIR}"

cat > "${DEMO_COMMANDS_FILE}" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail

cat > test.txt <<'TXT'
This test file contains test data.
We also mention pattern and pXttern for matching.
Another test line includes words from list.
TXT

cat > words.txt <<'TXT'
test
pattern
line
TXT

sleep 1
python word_counter.py --single-word "test" -s test.txt
sleep 1
python word_counter.py --pattern "p[a-z]ttern" -s test.txt
sleep 1
python word_counter.py --words-input-file words.txt -s test.txt
EOF

chmod +x "${DEMO_COMMANDS_FILE}"

asciinema rec --overwrite --idle-time-limit 1 --command "${DEMO_COMMANDS_FILE}" "${CAST_FILE}"
agg "${CAST_FILE}" "${GIF_FILE}"

echo "Created recording:"
echo " - ${CAST_FILE}"
echo " - ${GIF_FILE}"
