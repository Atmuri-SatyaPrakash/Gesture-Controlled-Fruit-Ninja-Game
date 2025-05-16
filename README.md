Bring Fruit Ninja to life — no keyboard or mouse needed! This fun mini-project lets you slice falling fruits with real-time hand gestures using your webcam. Built using OpenCV and MediaPipe, the game detects your hand movements and turns them into slicing actions. Perfect for showcasing interactive computer vision!

**🎮 Game Features**
✋ Real-time hand tracking with MediaPipe.

🍓 Randomly falling fruits — slice them before they fall off the screen.

⚔ Gesture slicing: Swipe quickly over fruits with your index finger to slice them.

❌ Missed fruits counter: Miss 3 and it's game over.

🧠 Swipe detection logic: Only fast hand swipes count — not just touching.

💬 Live HUD: Displays your score and how many fruits you’ve missed.

💣 Game Over screen: Shows when you miss 3 fruits.

🔁 Restart or Exit: After game over, press R to restart or Q to quit.

🍒 Smaller fruits for a more challenging experience.

**🧰 Requirements**

Make sure you have Python installed. Then install the required libraries:

pip install opencv-python mediapipe

**▶ How to Run the Game**

Clone or download this repository.

Open a terminal and navigate to the project folder:

cd gesture_fruit_ninja
(Optional) Install dependencies again if needed:

pip install opencv-python mediapipe

**Run the game:**

python main.py

Your webcam will activate, and the game window will appear.

**🕹 How to Play**

Make sure your hand is visible to the webcam.

Use your index finger to "slice" fruits — swipe quickly through them.

Slice as many fruits as possible. If you miss 3, it's game over.

On the Game Over screen, press:

R to restart the game

Q to quit the game

**🛠 Troubleshooting**

Webcam not working?

Make sure no other app is using the camera.

**Try changing the camera index:**

Replace cv2.VideoCapture(0) with cv2.VideoCapture(1) in the code.

**Hand not detected?**

Ensure good lighting.

Keep your hand clearly visible in the frame.

**Laggy or low FPS?**

Reduce webcam resolution in the code for smoother performance.
