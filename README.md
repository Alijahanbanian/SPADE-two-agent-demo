
# SPADE Two-Agent Communication Demo Project

This project demonstrates a simple agent-based communication model using the **SPADE library**. Two agents, a `ParentAgent` and a `ChildAgent`, communicate via messages. The `ParentAgent` sends a list of numbers to the `ChildAgent`, which calculates the sum and replies back with the result.

---

## Features

- Two autonomous agents (`ParentAgent` and `ChildAgent`) communicating over XMPP.
- Demonstrates message sending and receiving using SPADE.
- Dynamic behavior setup using SPADE's `OneShotBehaviour`.

---

## Prerequisites

- **Linux OS**
- Python 3.8 or higher
- An XMPP server (e.g., **Prosody**) set up and running locally.

---

## Installation

### 1. Install Python Dependencies

```bash
sudo apt update
sudo apt install python3 python3-pip
pip install spade
```

### 2. Set Up Prosody XMPP Server

1. **Install Prosody**  
   ```bash
   sudo apt install prosody
   ```

2. **Configure Prosody**  
   Edit the configuration file `/etc/prosody/prosody.cfg.lua`:
   ```lua
   VirtualHost "localhost"
   ```

3. **Add User Accounts**  
   Create users for the agents:
   ```bash
   sudo prosodyctl adduser Parent@localhost
   Password: password
   sudo prosodyctl adduser Child@localhost
   Password: password

   ```

4. **Restart Prosody**  
   ```bash
   sudo systemctl restart prosody
   ```

5. **Verify Prosody is Running**  
   Check the service status:
   ```bash
   sudo systemctl status prosody
   ```

---

## Usage

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/Alijahanbanian/SPADE-two-agent-demo.git
   cd spade-two-agent-demo
   ```

2. **Run the Script**  
   ```bash
   python3 main.py
   ```

3. **Expected Output**  
   - The `ParentAgent` sends numbers (`7,12`) to the `ChildAgent`.
   - The `ChildAgent` calculates the sum (`19`) and replies.
   - The `ParentAgent` prints the result.

---

## Code Overview

### Main Classes

- **ParentAgent**: Sends a message containing numbers to the `ChildAgent` and waits for the reply.
- **ChildAgent**: Receives a message, calculates the sum of the numbers, and replies.

### Key Methods

- `add_behaviour`: Adds behaviors to the agents.
- `Message`: Used for message creation and exchange between agents.

---

## Example Output

```plaintext
ParentAgent started ...
ParentAgent: ChildAgent started
ChildAgent: Sent result 19 to ParentAgent
ParentAgent: Result: 19
ParentAgent: ChildAgent stopped
ParentAgent finished !!!
```

---

## Troubleshooting

- **Issue**: No reply from `ChildAgent`.  
  **Solution**: Ensure the XMPP server is running and both agents' credentials (`Aos1@localhost`, `Aos2@localhost`) are correct.

- **Issue**: Cannot connect to the XMPP server.  
  **Solution**: Verify the Prosody configuration and ensure the server is accessible on `localhost`.

---

## License

This project is licensed under the MIT License.
