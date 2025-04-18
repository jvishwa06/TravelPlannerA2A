from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

flight_agent = Agent(
    name="flight_agent",
    model=LiteLlm("groq/llama3-8b-8192"),
    description="Suggests flight options for the user to a destination.",
    instruction=(
        "Given origin, destination, dates, number of passengers, and budget, suggest 2-3 suitable flight options. "
        "For each option, provide airline name, flight duration, price estimate, and notable features like layovers or class. "
        "Respond in plain English. Keep it concise and well-formatted."
    )
)

session_service = InMemorySessionService()
runner = Runner(
    agent=flight_agent,
    app_name="flight_app",
    session_service=session_service
)

USER_ID = "user_flight"
SESSION_ID = "session_flight"


async def execute(request):
    session_service.create_session(
        app_name="flight_app",
        user_id=USER_ID,
        session_id=SESSION_ID
    )
    prompt = (
        f"User is looking for flights from {request['origin']} to {request['destination']} departing on {request['start_date']}, "
        f"returning on {request['end_date']} with a budget of {request['budget']}. "
        f"Suggest 2-3 flight options, each with airline, duration, price, and features like layovers or class. "
        f"Respond in a readable, human-friendly format with clear sections and bullet points."
    )
    message = types.Content(role="user", parts=[types.Part(text=prompt)])
    async for event in runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=message):
        if event.is_final_response():
            response_text = event.content.parts[0].text
            return {"flights": response_text}


