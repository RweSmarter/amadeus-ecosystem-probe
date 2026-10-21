import os,json,shutil
h=os.path.expanduser("~")
def e(x): return os.path.exists(x)
def sz(x):
    try: return sum(f.lstat().st_size for f in os.scandir(x) if f.is_file())
    except Exception: return None
print(json.dumps({
"home":h,
"tdata":e(h+"/Library/Application Support/Telegram Desktop/tdata"),
"tdata_bytes":sz(h+"/Library/Application Support/Telegram Desktop/tdata"),
"postbox":e(h+"/Library/Group Containers/6N38VWS5BX.ru.keepcoder.Telegram"),
"telegram_app":e("/Applications/Telegram.app"),
"go":[p for p in["/opt/homebrew/bin/go","/usr/local/bin/go",h+"/go/bin/go"] if e(p)],
"brew":[p for p in["/opt/homebrew/bin/brew","/usr/local/bin/brew"] if e(p)],
"git":[p for p in["/usr/bin/git","/opt/homebrew/bin/git"] if e(p)],
"docker_bin":[p for p in["/usr/local/bin/docker","/opt/homebrew/bin/docker"] if e(p)],
"docker_sock":e("/var/run/docker.sock"),
"nodejs":[p for p in["/opt/homebrew/bin/node","/usr/local/bin/node"] if e(p)],
"npm":[p for p in["/opt/homebrew/bin/npm","/usr/local/bin/npm"] if e(p)],
"npx":[p for p in["/opt/homebrew/bin/npx","/usr/local/bin/npx"] if e(p)],
"gobin_dir":e(h+"/go/bin"),
"disk_free_gb":round(shutil.disk_usage(h).free/2**30,1)
}))