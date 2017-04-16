cp script/launch.py.template script/launch.py
# Make it executable
chmod +x script/launch.py
# Launch it through ssh.
# nohup ./script/launch.py > mlrlog 2>&1 &
./script/launch.py > mlrlog 2>&1
