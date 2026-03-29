📸 Live Camera-Based Picture Puzzle Generator

An interactive real-time application that captures live images from your webcam and converts them into sliding puzzle games (3×3, 4×4, 5×5) using computer vision techniques.

🚀 Features
📷 Capture live images using webcam
🧩 Generate puzzle grids (3×3, 4×4, 5×5)
🔄 Dynamic image slicing and tile rearrangement
⚡ Real-time processing using OpenCV
🎮 Interactive puzzle experience
🧠 Smooth and optimized performance
🛠️ Tech Stack
Python
OpenCV (cv2)
NumPy
📂 Project Structure
Live_Puzzle/
│── main.py
│── puzzle.py
│── utils.py
│── requirements.txt
│── README.md
⚙️ Installation
Clone the repository
git clone https://github.com/your-username/Live_puzzle.git
cd Live_puzzle
Install dependencies
pip install -r requirements.txt
▶️ Usage

Run the application:

python main.py
Webcam will open 📷
Capture an image
Select puzzle size (3×3 / 4×4 / 5×5)
Start solving the puzzle 🎯
🧠 How It Works
Captures image using OpenCV
Divides image into equal grid tiles
Shuffles tiles randomly
Displays puzzle for user interaction
