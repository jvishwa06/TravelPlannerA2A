from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

stay_agent = Agent(
    name="stay_agent",
    model=LiteLlm("groq/llama3-8b-8192"),
    description="Suggests accommodation options for the user at a destination.",
    instruction=(
        "Given a destination, dates, number of guests, and budget, suggest 2-3 suitable accommodation options. "
        "For each option, provide a name, a short description, price per night estimate, and notable amenities. "
        "Respond in plain English. Keep it concise and well-formatted."
    )
)

session_service = InMemorySessionService()
runner = Runner(
    agent=stay_agent,
    app_name="stay_app",
    session_service=session_service
)

USER_ID = "user_stay"
SESSION_ID = "session_stay"


async def execute(request):
    session_service.create_session(
        app_name="stay_app",
        user_id=USER_ID,
        session_id=SESSION_ID
    )
    prompt = (
        f"User is looking for accommodation in {request['destination']} from {request['start_date']} to {request['end_date']}, "
        f"with a budget of {request['budget']}. "
        f"Suggest 2-3 accommodation options, each with name, description, price per night, and amenities. "
        f"Respond in a readable, human-friendly format with clear sections and bullet points."
    )
    message = types.Content(role="user", parts=[types.Part(text=prompt)])
    async for event in runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=message):
        if event.is_final_response():
            response_text = event.content.parts[0].text
            return {"stays": response_text}


