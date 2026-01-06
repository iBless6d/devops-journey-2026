# 🇩🇪 My DevOps Journey to Germany

## 📅 [2026-01-06] Day 1: Linux Fundamentals & System Admin

### 📝 Summary
Kicked off the journey by mastering core Linux commands, user management, and service administration. The focus was on practical implementation in a Debian-based environment.

### 🧠 Technical Deep Dive

#### 🔹 L1: Navigation & File Management
- **Commands:** `ls -la` (list all + hidden), `cd`, `mkdir -p` (nested directories).
- **Safety:** Understood the danger of `rm -rf` (Recursive Force).
- **Practice:** Built a project structure `Germany_Ops/src/logs/secrets`.

#### 🔹 L2: Permissions & User Security
- **Concept:** Analyzed `rwx` (Read/Write/Execute) and the 4-2-1 rule.
- **Critical Comparison:** `777` (Insecure) vs `755` (Standard) vs `700` (Private).
- **Lab:**
  - Created user `hans`.
  - Granted `sudo` privileges.
  - Restricted access: Used `chmod 700` on `secrets` directory to block other users.

#### 🔹 L3: Text Manipulation & Logs
- **Tools:** `cat` (view), `less` (scroll), `head/tail` (start/end).
- **Debugging:** Used `grep` to extract a specific "CRITICAL" error from a large log file.

#### 🔹 L4: Package & Service Management
- **Package Manager:** `apt update`, `apt install`, `dpkg`.
- **Services:** `systemctl` (start, stop, enable, status).
- **Lab:**
  - Installed **Nginx** web server.
  - Installed **htop** for monitoring.
  - Verified Nginx memory usage (0.1%) using `htop` filter (F4).

### 🐛 Troubleshooting & Fixes
- **Issue:** Typos in directory creation (`Gaeramany` instead of `Germany`).
- **Fix:** Used `mv` to rename the directory correctly.
- **Issue:** `htop` command not found.
- **Fix:** Installed via `sudo apt install htop`.

---
*"Disziplin ist Freiheit."*