import time
import subprocess

counter = 1


def run_scheduler(counter):
    # Execute the Python module or script using subprocess
    subprocess.run(
        [
            "<path_for_python_in_virtual_env>",
            "-m",
            "forward_messages",
            str(counter),
        ]
    )


while True:
    # Delay for 1 hour
    run_scheduler(counter)
    time.sleep(3600)
    counter += 1
