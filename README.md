# GPTvsGPT

GPTvsGPT is a playful Python application that simulates a conversation between two AI Assistants with distinct personalities. This program leverages OpenAI's Assistant API to generate a back-and-forth dialogue on a specified topic, allowing each Assistant's unique character traits to shine through in the conversation. This is easily extendible with additional Assistant API capabilities such as function calls and retrieval. You can learn more about the OpenAI Assistant API [here](https://platform.openai.com/docs/assistants/overview).

Find me on X/Twitter at [@yoheinakajima](https://twitter.com/yoheinakajima).

## How it Works

The application creates two Assistants with predefined personalities and instructions. It initiates a thread for each Assistant and starts a conversation on a given topic. Each Assistant takes turns responding to the other, with the conversation dynamically unfolding in real-time. Once set up, set up your parameters and run like this:

```python
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

# Example usage (assistant 1, assistant 2, topic, number of messages):
converse(assistant_1_params, assistant_2_params, "global warming", 5)
```

## Getting Started

### Prerequisites

- Python 3.x
- OpenAI API key

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yoheinakajima/GPTvsGPT.git
cd GPTvsGPT
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Setting up Environment Variables
Before running the script, you must set your OpenAI API key as an environment variable. This can be done in the command line or by setting it in a .env file.

Command line method:

```bash
export OPENAI_API_KEY='your_api_key_here'
```

### Usage

Run the script with the following command:

```bash
python main.py
```

You can customize the personalities and topics directly in the script or build upon the code to create a more interactive experience.

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change. Being fully candid, I'm not great at staying up to date on my own repos.

## License

MIT
