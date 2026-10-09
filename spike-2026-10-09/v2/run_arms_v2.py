import json, os, subprocess
from concurrent.futures import ThreadPoolExecutor
S = "<scratchpad>/spike/v2"
tasks = json.load(open(f"{S}/tasks.json"))
os.makedirs(f"{S}/runs", exist_ok=True)
EXTRA = {"A": ["--append-system-prompt-file", "notools.md"], "B": ["--append-system-prompt-file", "notools_age.md"],
         "C": ["--setting-sources", "project", "--append-system-prompt-file", "notools.md"],
         "D": ["--setting-sources", "project", "--append-system-prompt-file", "notools_age.md"]}
jobs = [(t, a, r) for t in tasks for a in "ABCD" for r in (1, 2)]
def run(j):
    t, a, r = j
    base = f"{S}/runs/{t['id']}_{a}_r{r}"
    if os.path.exists(base + ".json") and os.path.getsize(base + ".json") > 0:
        return
    cmd = ["claude", "-p", t["prompt"], "--model", "sonnet", "--tools", "", "--strict-mcp-config",
           "--mcp-config", "empty_mcp.json", "--output-format", "json"] + EXTRA[a]
    try:
        p = subprocess.run(cmd, cwd=S, stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=300)
        out, err = p.stdout, p.stderr
    except subprocess.TimeoutExpired as e:
        out, err = "", "TIMEOUT"
    open(base + ".err", "w").write(err or "")
    if out:
        open(base + ".json", "w").write(out)
with ThreadPoolExecutor(4) as ex:
    list(ex.map(run, jobs))
