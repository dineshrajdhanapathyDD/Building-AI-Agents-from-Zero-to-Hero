# Challenge 1: Your First AI Agent 🤖

Build a simple AI agent using **Strands Agents SDK + Ollama** that runs 100% locally on your machine. No cloud, no API keys required.

| Stack | Details |
|-------|---------|
| SDK | [Strands Agents](https://github.com/strands-agents/sdk-python) |
| Model Provider | [Ollama](https://ollama.com/) (local) |
| Model | `llama3.2:3b` |
| Language | Python 3.10+ |

---

## What You'll Learn

- How to install and run Ollama locally
- How to connect Strands Agents SDK to a local model
- How to create an agent with a system prompt
- How to send a question and get a response

---

## Prerequisites

- Python 3.10 or higher
- Linux / macOS / WSL (Windows Subsystem for Linux)
- ~2 GB disk space for the model

---

## Step-by-Step Setup

### 1. Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

<details>
<summary>📸 What you should see (click to expand)</summary>

```
>>> Cleaning up old version at /usr/local/lib/ollama
[sudo] password for user:
>>> Installing ollama to /usr/local
>>> Downloading ollama-linux-amd64.tar.zst
############################################# 100.0%
>>> Adding ollama user to render group...
>>> Adding ollama user to video group...
>>> Adding current user to ollama group...
>>> Creating ollama systemd service...
>>> Enabling and starting ollama service...
>>> Nvidia GPU detected.
>>> The Ollama API is now available at 127.0.0.1:11434
>>> Install complete. Run "ollama" from the command line.
```

</details>

---

### 2. Verify Ollama is Running

Open your browser and navigate to `http://localhost:11434`. You should see:

```
Ollama is running
```

> 💡 If you try `ollama serve` and get the error below, that means Ollama is already running as a service — you're good to go!

<details>
<summary>📸 "Address already in use" error (click to expand)</summary>

```
$ ollama serve
Couldn't find '/home/user/.ollama/id_ed25519'. Generating new private key.
Your new public key is:
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIEDfSsGkuGtJt59jwk8CvbnFsjjLLuqT3hmPR1EQ44J9

Error: listen tcp 127.0.0.1:11434: bind: address already in use
```

This is fine — Ollama started automatically as a systemd service during installation.

</details>

---

### 3. Pull the Model

```bash
ollama pull llama3.2:3b
```

<details>
<summary>📸 Expected output (click to expand)</summary>

```
pulling manifest
pulling dde5aa3fc5ff: 100%    2.0 GB
pulling 966de95ca8a6: 100%    1.4 KB
pulling fcc5a6bec9da: 100%    7.7 KB
pulling a70ff7e570d9: 100%    6.0 KB
pulling 56bb8bd477a5: 100%    96 B
pulling 34bb5ab01051: 100%    561 B
verifying sha256 digest
writing manifest
success
```

</details>

---

### 4. Create a Virtual Environment

> ⚠️ **Common Error:** If you try to `pip install` directly on modern Linux/Debian systems, you'll hit this:

<details>
<summary>📸 "externally-managed-environment" error (click to expand)</summary>

```
$ pip install strands-agents strands-agents-tools
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.

    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
```

</details>

**Solution:** Always use a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate    # macOS/Linux
```

<details>
<summary>📸 Expected output (click to expand)</summary>

```
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $
```

Your prompt should now show `(venv)` at the beginning.

</details>

---

### 5. Install Dependencies

```bash
pip install strands-agents "strands-agents[ollama]" strands-agents-tools faiss-cpu
```

<details>
<summary>📸 Expected output (click to expand)</summary>

```
(venv) $ pip install strands-agents "strands-agents[ollama]" strands-agents-tools faiss-cpu
Collecting strands-agents
  Downloading strands_agents-1.40.0-py3-none-any.whl (19 kB)
Collecting strands-agents-tools
  Downloading strands_agents_tools-0.5.3-py3-none-any.whl (59 kB)
                              59.5/59.5 kB 1.7 MB/s eta 0:00:00
...
Successfully installed strands-agents strands-agents-tools ...
```

</details>

---

### 6. Run the Agent

```bash
python starter.py
```

<details>
<summary>📸 Expected output (click to expand)</summary>

```
(venv) $ python starter.py
Python is a high-level, interpreted programming language that is widely used for various purposes such as:

1. Web development (e.g., Django, Flask)
2. Data analysis and science (e.g., NumPy, Pandas, scikit-learn)
3. Artificial intelligence and machine learning (e.g., TensorFlow, Keras)
4. Automation and scripting
5. Game development

Python is known for its simplicity, readability, and ease of use, making it a great language
for beginners and experts alike. Its syntax is clean and concise, with a focus on code readability.

Some key features of Python include:

* Indentation-based syntax (no semicolons or brackets)
* Dynamic typing (no explicit type definitions)
* Extensive libraries and frameworks
* Cross-platform compatibility

Overall, Python is a versatile and popular language that has become an essential tool for many
professionals in the tech industry. 🤖 Agent: Python is a high-level, interpreted programming language...
```

</details>

---

## The Code

Here's the complete `starter.py`:

```python
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
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `error: externally-managed-environment` | Use a virtual environment: `python3 -m venv venv && source venv/bin/activate` |
| `Error: listen tcp 127.0.0.1:11434: bind: address already in use` | Ollama is already running as a service. This is fine — skip `ollama serve` |
| `Connection refused` on localhost:11434 | Run `ollama serve` in a separate terminal |
| Model not found | Run `ollama pull llama3.2:3b` first |
| Slow responses | The 3B model needs ~4 GB RAM. Close other apps if needed |
| `ModuleNotFoundError: No module named 'strands'` | Make sure your venv is activated and you ran `pip install` inside it |

---

## Bonus Challenges 🏴‍☠️


### 1. Ask Multiple Questions

```python
response = agent("What is Python?")
print(f"🤖 Agent: {response}")

response2 = agent("What is machine learning?")
print(f"🤖 Agent: {response2}")

response3 = agent("What is artificial intelligence?")
print(f"🤖 Agent: {response3}")
```

<!--<details>
<summary>📸 Sample output for "What is machine learning?" (click to expand)</summary>

```
(venv) $ python starter.py
Machine learning (ML) is a subset of artificial intelligence (AI) that enables computers to
learn from data without being explicitly programmed.

In traditional programming, code is written to perform a specific task. In contrast, machine
learning algorithms are designed to identify patterns and make predictions or decisions based
on large datasets. These algorithms can improve their performance over time as they receive
more data, making them increasingly accurate.

Machine learning involves three key processes:

1. **Data preparation**: Collecting and preprocessing data for training the model.
2. **Model training**: Feeding the prepared data into an algorithm to learn from it.
3. **Model evaluation**: Testing the trained model on new data to assess its performance.

There are several types of machine learning, including:

* **Supervised learning**: The algorithm learns from labeled data to make predictions.
* **Unsupervised learning**: The algorithm identifies patterns in unlabeled data.
* **Reinforcement learning**: The algorithm learns through trial and error by interacting
  with an environment.

Machine learning has numerous applications across industries, such as image recognition,
natural language processing, predictive maintenance, and more.
🤖 Agent: Machine learning (ML) is a subset of artificial intelligence...
```

</details>-->

![Screenshot 2026-05-21 134709.png](https://images.tomarkdown.dev/uploaded/825chxflt76hld9k.png)

![Screenshot 2026-05-21 134827.png](https://images.tomarkdown.dev/uploaded/f2ixz1agsrsji47z.png)

![Screenshot 2026-05-21 135007.png](https://images.tomarkdown.dev/uploaded/iczh3topesu0kw7f.png)

---

## Quick Reference

```bash
# Full setup in one go
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2:3b
python3 -m venv venv
source venv/bin/activate
pip install strands-agents "strands-agents[ollama]" strands-agents-tools faiss-cpu
python starter.py
```

---

## Project Structure

```
challenge-1-first-agent/
├── README.md
└── starter.py
```

---

## Resources

- [Strands Agents SDK Documentation](https://github.com/strands-agents/sdk-python)
- [Ollama Official Site](https://ollama.com/)
- [Ollama Model Library](https://ollama.com/library)
- [Python venv Documentation](https://docs.python.org/3/library/venv.html)

---

*Built as part of the AWS User Group MDU — May Skill Sprint 🚀*
