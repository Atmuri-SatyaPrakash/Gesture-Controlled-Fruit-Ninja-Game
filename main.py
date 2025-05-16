import cv2
import mediapipe as mp
import random
import time
import math

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1)

# Fruit class
class Fruit:
    def __init__(self, x, y, velocity):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.radius = 20
        self.alive = True

    def move(self):
        self.y += self.velocity
        if self.y > 480:
            self.alive = False

    def draw(self, frame):
        if self.alive:
            cv2.circle(frame, (self.x, self.y), self.radius, (0, 255, 0), -1)

def run_game():
    cap = cv2.VideoCapture(0)
    while True:
        fruits = []
        prev_x, prev_y = None, None
        last_spawn_time = time.time()
        score = 0
        missed = 0
        max_missed = 3

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.flip(frame, 1)
            h, w, _ = frame.shape

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb)

            curr_x, curr_y = None, None
            swipe = False

            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

                    x = int(handLms.landmark[8].x * w)
                    y = int(handLms.landmark[8].y * h)

                    curr_x, curr_y = x, y
                    cv2.circle(frame, (x, y), 10, (255, 0, 255), -1)

                    if prev_x is not None and prev_y is not None:
                        dist = math.hypot(curr_x - prev_x, curr_y - prev_y)
                        if dist > 20:
                            swipe = True

            if time.time() - last_spawn_time > 1:
                new_fruit = Fruit(random.randint(50, w - 50), 0, velocity=5)
                fruits.append(new_fruit)
                last_spawn_time = time.time()

            for fruit in fruits:
                fruit.move()
                fruit.draw(frame)

                if not fruit.alive and fruit.y >= 480:
                    missed += 1

                if swipe and fruit.alive and curr_x is not None:
                    distance = math.hypot(fruit.x - curr_x, fruit.y - curr_y)
                    if distance < fruit.radius:
                        fruit.alive = False
                        score += 1
                        cv2.putText(frame, "SLICED!", (fruit.x - 20, fruit.y),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            fruits = [fruit for fruit in fruits if fruit.alive]

            cv2.putText(frame, f"Score: {score}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, f"Missed: {missed}/{max_missed}", (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            if missed >= max_missed:
                while True:
                    game_over_frame = frame.copy()
                    cv2.putText(game_over_frame, "GAME OVER", (w//3, h//2 - 40),
                                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
                    cv2.putText(game_over_frame, "Press 'R' to Restart or 'Q' to Quit", (w//4, h//2 + 40),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.imshow("Fruit Ninja (Gesture)", game_over_frame)

                    key = cv2.waitKey(1) & 0xFF
                    if key == ord('r'):
                        fruits.clear()
                        score = 0
                        missed = 0
                        last_spawn_time = time.time()
                        prev_x, prev_y = None, None
                        break
                    elif key == ord('q'):
                        cap.release()
                        cv2.destroyAllWindows()
                        return

            prev_x, prev_y = curr_x, curr_y

            cv2.imshow("Fruit Ninja (Gesture)", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                return

if __name__ == "__main__":
    run_game()
