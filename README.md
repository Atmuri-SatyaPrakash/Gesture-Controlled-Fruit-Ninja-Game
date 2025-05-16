# Gesture-Controlled-Fruit-Ninja-Game

Bring Fruit Ninja to life — no keyboard or mouse needed! This fun mini-project lets you slice falling fruits with real-time hand gestures using your webcam. Built with OpenCV and MediaPipe, the game tracks your hand movements and turns them into slicing actions. Perfect for a quick interactive demo or just some creative fun with computer vision!

🎮 Game Features
✋ Real-time hand tracking using MediaPipe.

🍓 Fruits spawn randomly and fall from the top of the screen.

⚔ Slice fruits by swiping your hand across them — just like in the original game!

❌ Missed a fruit? Game over.

🧰 Requirements
Make sure you have Python installed, then install the required libraries:

bash
Copy
Edit
pip install opencv-python mediapipe
▶ How to Run the Game
Clone or download this repository.

Open a terminal or command prompt and navigate to the project folder:

bash
Copy
Edit
cd gesture_fruit_ninja
Install dependencies (if not done already):

bash
Copy
Edit
pip install opencv-python mediapipe
Run the game:

bash
Copy
Edit
python main.py
The game window will open, and your webcam will activate. Start slicing!

🕹 How to Play
Make sure your hand is visible in the webcam.

Use your index finger to "slice" — a fast swipe motion will slice any fruit it intersects.

The goal: Slice as many fruits as you can before one hits the bottom unsliced.

🛠 Troubleshooting
If the webcam doesn’t open or shows a black screen:

Make sure no other application is using your camera.

Try changing the webcam index in the code (e.g., cv2.VideoCapture(0) to cv2.VideoCapture(1)).

Hand not detected?

Use a well-lit background.

Ensure your hand is clearly visible in the camera frame.

Performance issues?

Try reducing the resolution of the webcam capture for smoother gameplay.
