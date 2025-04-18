# TravelPlannerA2A

## Overview
Travel Planner Agent2Agent is a multi-agent AI system that orchestrates travel planning using Agent-to-Agent (A2A) communication. This application demonstrates how specialized AI agents can collaborate to produce comprehensive travel itineraries based on user preferences.

The system features specialized agents for flights, accommodation, and activities that work together, coordinated by a host agent, to deliver a complete travel plan through a user-friendly interface.

## Features
- **Multi-Agent Architecture**: Specialized agents handle different aspects of travel planning
- **Agent-to-Agent Communication**: Agents communicate via a simple HTTP-based protocol
- **Interactive UI**: Streamlit-based interface for inputting travel preferences and displaying results
- **LLM Integration**: Uses Google ADK and Groq's Llama3-8b model for generating intelligent recommendations

### Components:
1. **Host Agent (Port 8000)**: Orchestrates the communication between specialized agents
2. **Flight Agent (Port 8001)**: Recommends flight options based on user criteria
3. **Stay Agent (Port 8002)**: Suggests accommodation options at the destination
4. **Activities Agent (Port 8003)**: Recommends activities and attractions at the destination
5. **Streamlit UI**: Provides an interface for user inputs and displaying results

### Communication Flow:
1. User submits travel preferences via the Streamlit UI
2. Request is sent to the Host Agent
3. Host Agent distributes the request to specialized agents
4. Each agent processes the request and returns recommendations
5. Host Agent compiles all responses and returns them to the UI
6. Results are displayed to the user

## Installation

### Prerequisites
- Python 3.10+
- pip package manager

### Setup
1. Clone the repository:
```bash
git clone <repository-url>
cd GoogleA2A
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
python main.py
```
This will start:
- All agent servers on their respective ports
- The Streamlit UI (typically on http://localhost:8501)

2. Open the Streamlit UI in your browser and input:
- Origin location
- Destination
- Start and end dates
- Budget

3. Click "Plan My Trip" to receive a comprehensive travel plan with:
- Flight recommendations
- Accommodation options
- Activity suggestions

## Project Structure
```
.
├── main.py                 # Main entry point and service launcher
├── travel_ui.py            # Streamlit UI implementation
├── requirements.txt        # Project dependencies
├── agents/                 # Agent implementations
│   ├── host_agent/         # Orchestrator agent
│   ├── flight_agent/       # Flight recommendation agent
│   ├── stay_agent/         # Accommodation recommendation agent
│   └── activities_agent/   # Activities recommendation agent
├── common/                 # Shared utilities
│   ├── a2a_client.py       # Agent-to-agent communication client
│   └── a2a_server.py       # Agent server implementation
└── shared/                 # Shared data models
    └── schemas.py          # Pydantic data schemas
```

## Implementation Details

### Agent Structure
Each agent follows a similar structure:
- `__main__.py`: Entry point that creates the FastAPI app
- `agent.py`: Agent implementation using Google ADK
- `task_manager.py`: Task execution logic

### A2A Communication
The system implements a simple but effective Agent-to-Agent communication protocol:
- REST-based API using FastAPI
- Standardized request/response format
- Asynchronous communication using httpx

## Future Enhancements
- Integration with real travel APIs
- User authentication and saved preferences
- More specialized agents (e.g., car rentals, travel insurance)
- Support for multi-leg trips and complex itineraries

## Acknowledgements
- Google ADK Team
- Groq for LLama3 model access
- FastAPI, Streamlit, and other open-source libraries used in this project