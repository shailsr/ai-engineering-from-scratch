# Safe shell helpers for AI Engineering from Scratch.

# Activate the virtual environment from a project root.
alias ae='source .venv/bin/activate'

# Disk usage.
alias diskuse='df -h .'

# tmux shortcuts.
alias ta='tmux attach -t'
alias tls='tmux ls'
alias tn='tmux new -s'
alias tk='tmux kill-session -t'

# Show the largest memory-consuming processes.
memhogs() {
    ps aux -m | head -11
}

# Search running processes by name.
psg() {
    if (( $# == 0 )); then
        echo "Usage: psg <process-name>"
        return 1
    fi

    ps aux |
        grep -v grep |
        grep -i -- "$1"
}

# Follow log files and show lines matching a pattern.
watchlog() {
    local pattern="${1:-loss}"
    local log_files=(logs/*.log(N))

    if (( ${#log_files[@]} == 0 )); then
        echo "No log files found under ./logs/"
        return 1
    fi

    tail -f "${log_files[@]}" |
        grep --line-buffered -E "$pattern"
}
