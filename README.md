# Vector and Matrix Operations Project

This Python project demonstrates various **vector and matrix operations** using **NumPy**, and visualizes **2D vectors** using **Matplotlib**.

---

## 🚀 Features

* Vector operations:

  * Addition, Subtraction
  * Dot Product
  * Magnitude Calculation

* Matrix operations:

  * Addition, Subtraction
  * Multiplication
  * Transpose
  * Determinant

* Visualization of 2D vectors

* Clean and modular code structure

---

## 📦 Installation

1. **Clone this repository**:

   ```bash
   git clone <your-repo-url>
   cd vector-matrix-operations
   ```

2. **Create and activate a virtual environment** (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🧠 Usage

Run the main script:

```bash
python vector_operations.py
```

This will:

* Perform various **vector operations**
* Perform **matrix operations**
* Generate a **2D vector plot** and save it in the `images/` directory

---

## ✏️ Customization

You can modify the vectors and matrices in `vector_operations.py`:

* Change the vectors in the `plot_vectors()` function
* Modify the matrices in the `perform_matrix_operations()` function

---

## 📁 Folder Structure

```
vector-matrix-operations/
├── vector_operations.py       # Main script with logic
├── requirements.txt           # List of required packages
├── README.md                  # Project documentation
├── .gitignore                 # Files/folders to ignore
└── images/                    # Folder for saved plots
```

---

## 🔧 .gitignore

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class

# IDEs
.idea/
.vscode/

# Virtual Environments
venv/
env/

# Output files
images/
*.png

# System files
.DS_Store
```

---

## 🔬 Dependencies

* Python 3.7+
* NumPy
* Matplotlib

All dependencies are listed in `requirements.txt`.

```txt
numpy
matplotlib
```

---

## 📌 How to Use This Project

1. Create the project directory and add all required files:

   * `vector_operations.py`
   * `requirements.txt`
   * `README.md`
   * `.gitignore`
   * `images/` folder

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the script:

   ```bash
   python vector_operations.py
   ```

The script will:

* Perform vector operations and print the results
* Perform matrix operations and print the results
* Generate and save a vector visualization plot in the `images/` directory

You can easily experiment with different values by editing the code.

---

## 📝 License

This project is open source and available under the **MIT License**.

---

Built with ❤️ using Python, NumPy & Matplotlib. Happy computing! 🧮📈
