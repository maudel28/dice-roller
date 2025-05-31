# 🎲 Dice Roller (Flask App)

Welcome to **Dice Roller** — a fun and simple web app where you click a button and watch the dice roll with animation before showing a random result! Built using **Python Flask** and styled with pure **HTML/CSS** magic ✨

---

## 🚀 Clone this Repo

You can get started by cloning this repository:

```bash
git clone https://github.com/maudel28/dice-roller.git
cd dice-roller
````

---

## ⚙️ Configuration (config.yaml)

This app uses a `config.yaml` file to customize its look and behavior without changing the code. Here's what each variable does:

```yaml
background_color: "#ffffff"      # Background color of the webpage
button_color: "#4CAF50"          # Color of the "Roll Dice" button
dice_color: "#47A9FF"            # Default color for all dice faces
dice_color_result: "#f23f3f"     # Color of the dice face when showing the final result
spin_duration: 3                 # Duration (in seconds) the dice will animate before stopping
```

🎨 Use this file to easily change the look of your app for different environments (e.g., dev, test, prod)!

---

## 🐳 Running with Docker

Although this project doesn't include a `Dockerfile` by default, here's how you can run the app using **Python 3.9** and **bind mount** the project directory.

### 🧱 1. Create a `Dockerfile`

Create a file called `Dockerfile` in the root folder:

```bash
cd dice-roller
vim Dockerfile
```

and paste this content:

```Dockerfile
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy only the requirements file (code will be mounted at runtime)
COPY requirements.txt /app/

# Create a virtual environment in a dedicated folder
RUN python -m venv /opt/venv

# Install dependencies inside the virtual environment
RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Add the virtual environment to the PATH so "python" and "pip" point to the venv versions
ENV PATH="/opt/venv/bin:$PATH"

# Expose the port used in the Flask app
EXPOSE 8080

# Start the Flask app
CMD ["python", "app.py"]
```

> 📝 Note: We only copy `requirements.txt` — the actual app files will be **mounted at runtime**!

---

### 📦 2. Build the Docker Image

Open your terminal inside the project folder and run:

```bash
docker build -t dice-roller .
```

This command creates an image named `dice-roller` with all necessary Python dependencies.

---

### ▶️ 3. Run the Container with Bind Mount

Now run the container and mount your local code folder into the container:

```bash
docker run -d \
  -p 80:8080 \
  -v /path/to/dice-roller/:/app/:ro \
  --name my-dice-app \
  dice-roller
```

> Replace `/path/to/dice-roller/` with the full path where you cloned this repo.

🌀 Why -p 80:8080?

Because the app runs on port **8080** inside the container (`app.py` uses `port=8080`), and we want to map it to port **80** on your machine.

✅ This lets you:

* Keep your code and config on your machine.
* Edit `config.yaml` or HTML files live.
* Restart the container to apply changes — **no rebuild needed!**

---

## 🌐 Open in Your Browser

Once the container is running, just visit:

```
http://localhost
```

You’ll see the 🎲 emoji ready to roll — click it and enjoy the animation!

---

## 🔁 Restart to Apply Changes

If you update `config.yaml` or any app file:

```bash
docker restart my-dice-app
```

This reloads the app with your new config without rebuilding the image.

---

## 🧹 Stop & Remove Container (Optional)

```bash
docker stop my-dice-app
docker rm my-dice-app
```

---

## 💡 Tips

* You can customize styles using the `config.yaml` file.
* Try creating different `git` branches with different configurations (e.g., dev/test/prod).
* Use this as a base for more complex Flask projects!

---

Have fun! 🎲✨
