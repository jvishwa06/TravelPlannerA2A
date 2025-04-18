"""
Main entry point for the Google A2A Travel application.
This script starts all agent servers and the Streamlit UI.
"""

import subprocess
import time
import sys
import signal
import atexit

processes = []

def cleanup():
    """Terminate all child processes when the main script exits."""
    print("\nShutting down all services...")
    for process in processes:
        if process.poll() is None:
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
    print("All services have been shut down.")

def start_service(command, name):
    """Start a service with the given command and name."""
    print(f"Starting {name}...")
    process = subprocess.Popen(command, shell=False)
    processes.append(process)
    return process

def main():
    """Main function to start all services."""
    atexit.register(cleanup)
    
    signal.signal(signal.SIGINT, lambda sig, frame: sys.exit(0))
    signal.signal(signal.SIGTERM, lambda sig, frame: sys.exit(0))
    
    host_cmd = ["uvicorn", "agents.host_agent.__main__:app", "--port", "8000"]
    start_service(host_cmd, "host agent")
    time.sleep(2)
    
    flight_cmd = ["uvicorn", "agents.flight_agent.__main__:app", "--port", "8001"]
    start_service(flight_cmd, "flight agent")
    time.sleep(2)
    
    stay_cmd = ["uvicorn", "agents.stay_agent.__main__:app", "--port", "8002"]
    start_service(stay_cmd, "stay agent")
    time.sleep(2)
    
    activities_cmd = ["uvicorn", "agents.activities_agent.__main__:app", "--port", "8003"]
    start_service(activities_cmd, "activities agent")
    time.sleep(2)
    
    print("Starting Streamlit UI...")
    streamlit_cmd = ["streamlit", "run", "travel_ui.py"]
    streamlit_process = subprocess.Popen(streamlit_cmd, shell=False)
    processes.append(streamlit_process)
    
    try:
        streamlit_process.wait()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, shutting down...")
        sys.exit(0)

if __name__ == "__main__":
    main()
