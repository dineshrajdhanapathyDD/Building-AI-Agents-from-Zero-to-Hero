from strands import Agent
from strands.models.ollama import OllamaModel

# Configure the Ollama model (runs locally)
model = OllamaModel(
    host="http://localhost:11434",
    model_id="llama3.2:3b"
)

# Create the agent with a system prompt
agent = Agent(
    model=model,
    system_prompt="You are a helpful AI assistant. Answer questions clearly and concisely.",
    tools=[]
)

# Send a question and print the response
response = agent("What is Python?")
print(f"🤖 Agent: {response}")

#response2 = agent("What is machine learning?")
#print(f"🤖 Agent: {response2}")

#response3 = agent("What is artificial intelligence?")
#print(f"🤖 Agent: {response3}")