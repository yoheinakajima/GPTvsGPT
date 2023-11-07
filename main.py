import time
import threading
import os
import openai
from openai import OpenAI

client = OpenAI()
client.api_key = os.environ.get('OPENAI_API_KEY')

def get_last_assistant_message(thread_id):
    messages_response = client.beta.threads.messages.list(thread_id=thread_id)
    messages = messages_response.data
  
    # Iterate through messages in reverse chronological order to find the last assistant message
    for message in messages:
        if message.role == 'assistant':
            # Get the content of the last assistant message
            assistant_message_content = " ".join(
                content.text.value for content in message.content if hasattr(content, 'text')
            )
            return assistant_message_content.strip()
  
    return ""  # Return an empty string if there is no assistant message

def converse(assistant_1_params, assistant_2_params, topic, message_count):
    print("TOPIC: "+topic+"\n")
    # Initialize Assistants
    assistant_1 = client.beta.assistants.create(**assistant_1_params)
    assistant_2 = client.beta.assistants.create(**assistant_2_params)

    # Create Threads
    thread_1 = client.beta.threads.create()
    thread_2 = client.beta.threads.create()

    # Function for the conversation between two assistants
    def assistant_conversation(start_message, assistant_a, thread_a, assistant_b, thread_b, msg_limit):
      message_content = start_message
      last_user_message_id = None  # Initialize with no last user message
  
      for i in range(msg_limit):
          # Determine which assistant is speaking for color coding
          if assistant_a == assistant_1:
              assistant_color = '\033[94m\033[1m' 
              assistant_name = assistant_1_params.get('name')
          else:
              assistant_color = '\033[92m\033[1m'
              assistant_name = assistant_2_params.get('name')
  
          # Bold and color the assistant's name and print the turn
          print(f"{assistant_color}{assistant_name} speaking...\033[0m (Turn {i + 1})")
  
          # Send the message and wait for a response
          user_message = client.beta.threads.messages.create(
              thread_id=thread_a.id,
              role="user",
              content=message_content
          )
  
          # Run the assistant and wait until it's done
          run = client.beta.threads.runs.create(
              thread_id=thread_a.id,
              assistant_id=assistant_a.id
          )
          while True:
              run_status = client.beta.threads.runs.retrieve(
                  thread_id=thread_a.id,
                  run_id=run.id
              )
              if run_status.status == 'completed':
                  break
              time.sleep(1)  # sleep to avoid hitting the API too frequently
  
          # Get all messages from the assistant since the last 'user' message
          message_content = get_last_assistant_message(thread_a.id)
  
          # Print out each of the assistant's messages
          print(message_content+"\n")
  
          # Swap the assistants and threads for the next turn in the conversation
          assistant_a, assistant_b = assistant_b, assistant_a
          thread_a, thread_b = thread_b, thread_a


    # Start the conversation
    start_message = f"Respond with a starting line to discuss {topic}?"
    conversation_thread = threading.Thread(
        target=assistant_conversation,
        args=(start_message, assistant_1, thread_1, assistant_2, thread_2, message_count)
    )
    conversation_thread.start()
    conversation_thread.join()

# Define the parameters for the two assistants (example parameters provided)
assistant_1_params = {
    'name': "Pirate",
    'instructions': "You are a mean pirate.",
    'tools': [{"type": "code_interpreter"}],
    'model': "gpt-3.5-turbo-1106"
}

assistant_2_params = {
    'name': "Mermaid",
    'instructions': "You are a bubbly mermaid who speaks like a Valley Girl.",
    'tools': [{"type": "code_interpreter"}],
    'model': "gpt-3.5-turbo-1106"
}

# Example usage:
converse(assistant_1_params, assistant_2_params, "global warming", 5)
