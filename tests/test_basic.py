import subprocess
import json

def run_command(cmd):
    print(f">>> {cmd}")
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(result.stdout.decode(), result.stderr.decode())
    return result

# Enqueue a job
run_command('python -m queuectl.cli enqueue \'{"id":"test1","command":"false"}\'')
# List pending jobs
run_command('python -m queuectl.cli list --state pending')
# Start a worker (this should retry the job, then DLQ it)
run_command('python -m queuectl.cli worker start --count 1')

# After this, you can check DLQ
run_command('python -m queuectl.cli dlq list')
# Retry the DLQ job
run_command('python -m queuectl.cli dlq retry test1')
# Check pending again
run_command('python -m queuectl.cli list --state pending')
