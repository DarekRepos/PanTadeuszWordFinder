#!/usr/bin/env bash
set -euo pipefail

OUTPUT_DIR="${OUTPUT_DIR:-/output}"
CAST_FILE="${OUTPUT_DIR}/word_counter_demo.cast"
GIF_FILE="${OUTPUT_DIR}/word_counter_demo.gif"
DEMO_COMMANDS_FILE="/tmp/demo_commands.sh"

mkdir -p "${OUTPUT_DIR}"
cd /app

cat > sample.txt <<'TXT'
Apple trees grow near the old river bank.
banana bread tastes better with ripe banana slices.
A child carries an apple and a cherry to school.
Some lines mention cherry pie and apple jam.
No fruits here, just random words for testing.
Another banana appears in this sentence.
cherry blossoms bloom every spring morning.
apple banana cherry appear together in this line.
We also add kiwi, mango, and peach for variety.
The final line repeats apple and banana once more.
TXT

cat > words.txt <<'TXT'
apple
cherry
nonexistent
TXT

cat > "${DEMO_COMMANDS_FILE}" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail
export TERM="${TERM:-xterm-256color}"

type_cmd() {
  local cmd="$1"
  printf "%s\n" "${cmd}" | pv -qL 40
}

cd /app
if ! clear 2>/dev/null; then
  printf '\033c'
fi
echo "=== Word Counter CLI Demo ==="
sleep 1

type_cmd "python3 /app/word_counter.py --help"
python3 /app/word_counter.py --help
sleep 1

type_cmd "python3 /app/word_counter.py --single-word \"apple\" -s sample.txt"
python3 /app/word_counter.py --single-word "apple" -s sample.txt
sleep 1

type_cmd "python3 /app/word_counter.py --pattern \"b[a-z]+na\" -s sample.txt"
python3 /app/word_counter.py --pattern "b[a-z]+na" -s sample.txt
sleep 1

type_cmd "python3 /app/word_counter.py --words-input-file words.txt -s sample.txt"
python3 /app/word_counter.py --words-input-file words.txt -s sample.txt
EOF

sed -i 's/\r$//' "${DEMO_COMMANDS_FILE}"
chmod +x "${DEMO_COMMANDS_FILE}"
asciinema rec --overwrite --idle-time-limit 1 --command "bash ${DEMO_COMMANDS_FILE}" "${CAST_FILE}"

agg "${CAST_FILE}" "${GIF_FILE}"

echo "Created recording:"
echo " - ${CAST_FILE}"
echo " - ${GIF_FILE}"
