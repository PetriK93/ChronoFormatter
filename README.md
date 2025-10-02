![Preview](https://github.com/user-attachments/assets/ea98e9d6-dd7f-4ac5-9c67-fba59c161369)

ChronoFormatter is a simple desktop tool built with Python, Tkinter, and CustomTkinter for renaming image and video files in bulk.
It provides a clean interface where you can choose a folder, apply a date format, add an optional prefix, and quickly rename your files.

✨ Features

🗂 Choose a folder containing images or videos.

📝 Add a prefix (e.g., Vacation, ProjectX).

📅 Select a date format:

ISO (YYYY-MM-DD)

EU (DD-MM-YYYY)

US (MM-DD-YYYY)

🎞 Choose file type: Images or Videos.

👀 Live preview of the new filename before renaming.

🌗 Dark and light mode toggle with saved preferences.

✅ Success and warning dialogs to guide you.

🚀 Installation

1. Clone the repository  
   git clone https://github.com/PetriK93/ChronoFormatter.git  
   cd ChronoFormatter

2. Create a virtual environment (optional but recommended)  
   python -m venv venv  
   source venv/bin/activate # On Linux / macOS  
   venv\Scripts\activate # On Windows

3. Install these libraries  
   pip install customtkinter pillow

4. Run the app  
   python main.py

How to use the app

1. Enter a prefix (optional).

2. Select a date format.

3. Choose whether to rename images or videos.

4. Pick a folder containing your files.

5. Click Rename files.

Your files will be renamed automatically with the chosen format. 🎉

📦 Dependencies

Python 3.8+

customtkinter

Pillow (PIL)

Tkinter (comes with Python standard library)

📝 License

This project is open source under the MIT License.
