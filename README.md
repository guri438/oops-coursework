# 🎮 Dodger Game (Python, Pygame)

## 📌 Introduction

### Purpose and Objectives
This project is a simple arcade-style game developed using Python and the Pygame library. The objective is to help the player avoid falling obstacles for as long as possible. The player earns points by surviving and avoiding the obstacles.

### Project Overview
The "Dodger Game" is a beginner-friendly project that demonstrates fundamental concepts of **Object-Oriented Programming (OOP)**, game loops, event handling, collision detection, and graphical interface development using Pygame.

---

## ❗ Problem Definition and Requirements

### Problem Description
Traditional console-based games are limited in interactivity and visual feedback. This application aims to solve that by creating a visually engaging and interactive experience where players must dodge falling obstacles to score points.

### Functional Requirements
- Move a player character (black square) left or right.
- Spawn red obstacles that fall from the top of the screen.
- Detect collision between the player and obstacles.
- Increase score when obstacles are avoided.
- Display Game Over screen with score and option to restart.

### Non-Functional Requirements
- Game runs smoothly at 60 FPS.
- Responsive to keyboard input (arrow keys and space bar).
- Simple and clear visual interface.
- Modular and readable code for maintainability.

---

## 🧠 Design and Implementation

### Object-Oriented Design Principles
While the current version is procedural, the code can be extended to use OOP by encapsulating entities like `Player`, `Obstacle`, and `Game` into classes. The current design:
- Demonstrates separation of concerns (drawing, logic, scoring).
- Makes use of functions to handle game components.

### Class Diagram (Future Design Suggestion)


### Key Algorithms and Structures
- **Collision Detection**: Uses `pygame.Rect.colliderect()` to detect overlap between player and obstacles.
- **Event Loop**: Processes user input and game updates in real-time.
- **Obstacle Management**: Spawns new obstacles at intervals and removes them when off-screen.
- **Score Calculation**: Increments score when player avoids obstacles.

---

## 🛠️ Development Process

### Tools and Environment
- **Language**: Python 3.x
- **Library**: Pygame
- **IDE**: Visual Studio Code / PyCharm
- **Operating System**: Windows/Linux

### Development Steps
1. Initialize Pygame and define game settings.
2. Create player and obstacle drawing functions.
3. Implement game loop with keyboard input.
4. Add collision detection and score tracking.
5. Design Game Over screen and restart logic.
6. Test and validate the application.

---

## 🚀 Results and Demonstration

### Key Features
- Responsive movement with left/right arrow keys.
- Randomly falling red obstacles.
- Real-time score tracking.
- Restartable game session after a collision.

### Screenshots

| In-Game View                         | Game Over Screen                   |
|-------------------------------------|------------------------------------|
| ![Game Screenshot](images/game.png) | ![Game Over](images/gameover.png)  |

> Replace the above with actual screenshots or assets from your project directory.

---

## ✅ Testing and Validation

### Testing Procedures
- Manual testing with different key inputs.
- Edge case testing: Moving to screen boundaries.
- Collision detection testing by positioning player under falling objects.

### Test Results
- Game runs smoothly at 60 FPS.
- Player movement and boundaries function correctly.
- Game over logic triggers accurately on collision.
- Restart mechanism works as expected.

### Issues Resolved
- Fixed bug where obstacles were modified during iteration (used list slicing).
- Ensured player doesn't move off-screen.
- Added `pygame.quit()` only once to avoid errors.

---

## 🧾 Conclusion and Future Work

### Summary of Achievements
- Successfully created a playable and engaging game using Pygame.
- Demonstrated understanding of event handling, rendering, and game logic.
- Implemented modular and readable code structure.

### Future Improvements
- Convert to full OOP design using `Player`, `Obstacle`, and `Game` classes.
- Add difficulty scaling (increase speed over time).
- Add power-ups, levels, or lives.
- Integrate background music and sound effects.
- Deploy as a desktop executable or web game (via PyInstaller or Pygbag).

---

## 📂 Project Structure


