# Phase 00 — Terminal and Shell

## Environment

- Platform: macOS on Apple Silicon
- Shell: zsh 5.9
- Python environment: repository `.venv`
- tmux: 3.7c
- htop: 3.5.3
- watch: procps-ng 4.0.7

## Shell fundamentals

Practised:

- `Ctrl+C` to interrupt a foreground process
- `Ctrl+Z` to suspend a foreground process
- `jobs` to list shell-managed jobs
- `fg %1` to resume a suspended job
- `&` to start a background process
- `$!` to obtain the latest background PID
- `wait` to wait for a background process and retrieve its exit status
- `ps` to inspect running processes

## Pipes and redirection

Practised:

- `command1 | command2` to pipe output between commands
- `>` to create or overwrite a file
- `>>` to append to a file
- `2>` to redirect standard error
- `2>&1` to combine standard error with standard output
- `tee` to display output and save it simultaneously

Used `grep`, `awk`, `wc`, `head`, `tail`, `sort`, and `cat` to inspect and process training logs.

## Background and persistent processes

Ran a Python job in the background and inspected its PID and status.

Ran a simulated training process with `nohup`, redirected its output to a log, and monitored the log with `tail -f`.

Stopping `tail -f` with `Ctrl+C` stopped only the log viewer, not the background training process.

## tmux

Created a `shell-lesson` tmux session with three panes:

1. `htop` for process and resource monitoring
2. `watch date` for periodically repeated output
3. A Python training simulation

Detached from the session, confirmed that its processes continued, reattached successfully, and then removed the completed session.

## Shell aliases

Created a macOS-safe zsh helper file containing:

- `ae` for activating the repository `.venv`
- `diskuse` for checking available disk space
- tmux session shortcuts
- `memhogs` for viewing memory-consuming processes
- `psg` for searching processes
- `watchlog` for filtering live log output

The helper file is sourced by `~/.zshrc`. A backup of the previous `.zshrc` was created before editing it.

GPU-specific aliases and broad process-killing commands from the supplied example were deliberately excluded because this Mac has no NVIDIA GPU and broad process matching can be unsafe.

## Training-log exercise

Generated a 100-line simulated training log.

Verified:

- 100 epoch records were created
- 100 loss values were extracted
- First/largest loss: `1.0000`
- Last/smallest loss: `.0100`
- `.0100` is equivalent to `0.0100`

## SSH configuration

Created and validated an example SSH configuration named `local-practice`.

Verified effective settings:

- Hostname: `localhost`
- User: `rathore`
- Port: `22`
- Server-alive interval: `60`
- Server-alive count maximum: `3`

A real remote GPU host, credentials, and port forwarding are deferred until a remote server is available.

## File transfer

Practised transfers with local temporary directories:

- `scp` for a straightforward one-time file copy
- `cmp` for verifying byte-for-byte equality
- `rsync -avn` for previewing synchronization
- `rsync -av` for performing synchronization
- Repeated `rsync` after changing the source file

Remote syntax follows the `user@host:/path` pattern, but no real remote transfer was attempted.

## Artifacts

- `personal-projects/phase-00/terminal-and-shell-demo/training_demo.py`
- `personal-projects/phase-00/terminal-and-shell-demo/shell_aliases.zsh`
- `personal-projects/phase-00/terminal-and-shell-demo/ssh_config.example`

Temporary logs, transfer copies, credentials, SSH keys, and machine-specific shell configuration are not committed.
