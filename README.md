# Budget-Tracker-System


This is a simple budget tracker app with a graphical user interface. You can:

- Add a total budget
- Add daily expenses
- View all expenses in a table
- See your remaining budget
- Reset all data

Tech Used:

- Python
- PySide6 (GUI)
- MySQL (to save expenses)
- JSON (to save budget)
- Pandas (to show data in a table)

📂 How to Run

1. Install the needed Python packages:
```bash
pip install PySide6 pandas mysql-connector-python
```

2. Make sure you have a MySQL database with this:
   ```sql
    CREATE DATABASE budget_system_db;

    USE budget_system_db;

    CREATE TABLE expenses (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        amount INT,
        date_exp DATE
    );
    ```
3. Run the app:
   ```bash
   python main.py
   ```

Take Note:
  - Your total budget and expenses are saved in `totalBudget.json`\
  - Your list of expenses is saved in MySQL

Created by: Mekier


