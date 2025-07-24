🚢 DockerAPI 🌊
Welcome to DockerAPI — your friendly Node.js library for managing Docker containers effortlessly! 🐳✨

🔥 What is DockerAPI?
DockerAPI is a lightweight, easy-to-use Node.js package that lets you control Docker containers programmatically. Whether you're building dev tools, automation scripts, or server management utilities, DockerAPI makes interacting with Docker a breeze! 🚀

🚀 Features
🐳 Start, stop, and manage Docker containers with simple API calls

⚡ Lightweight and fast

🧩 Minimal dependencies

📦 Fully supports common Docker operations

📝 Clear and easy-to-use API

🛠️ Installation
Install via npm:

bash
Copy
Edit
npm install dockerapi
💡 Usage
Here’s a quick example to get you started:

js
Copy
Edit
const DockerAPI = require('dockerapi');

const docker = new DockerAPI();

// List all containers
docker.listContainers()
  .then(containers => console.log(containers))
  .catch(err => console.error('Error:', err));
📚 API Reference
listContainers() — Lists all running containers 🏃‍♂️

startContainer(id) — Starts a container by ID ▶️

stopContainer(id) — Stops a container by ID ⏹️

removeContainer(id) — Removes a container by ID ❌

...and more!

Check out the source for full details.

🤝 Contributing
Contributions welcome! Feel free to open issues or submit pull requests. Let’s make DockerAPI even better together! 💪🐳

⚖️ License
This project is licensed under the MIT License. 📄

📫 Contact
Created by Angus Carr. Reach out if you want to chat or collaborate! ✉️

⭐️ Star the repo if you like it! Thanks for stopping by! 🙌
