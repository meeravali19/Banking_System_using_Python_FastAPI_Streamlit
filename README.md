# Banking System Using Python,FastAPI & Streamlit

This project is a full-stack banking application that combines the power of FastAPI for backend services and Streamlit for an intuitive frontend interface. It offers essential banking functionalities such as user registration, authentication, account management, and administrative controls.

## 🚀 Features

* **User Authentication:** Secure sign-up and login functionalities with password hashing.​

* **Account Management:** Users can view and manage their account details seamlessly.​

* **Admin Dashboard:** Administrative interface to oversee user activities and manage system operations.​

* **Interactive UI:** Streamlit-powered frontend for a responsive and user-friendly experience.​

* **Modular Architecture:** Clean separation of concerns with distinct modules for models, schemas, CRUD operations, and routing.​


## 🛠️ Technologies Used

* **Python:** Core programming language.​

* **FastAPI:** High-performance web framework for building APIs.​

* **Streamlit:** Framework for creating interactive web applications.​

* **SQLite:** Lightweight relational database for data storage.​

* **SQLAlchemy:** ORM for database interactions.​

* **Pydantic:** Data validation and settings management using Python type annotations.

## 📁 Project Structure
```sh
├── admindashboard.py      # Admin interface logic
├── crud.py                # CRUD operations for database models
├── database.py            # Database connection and session management
├── faq.py                 # Frequently Asked Questions module
├── images/                # Directory for storing image assets
├── login.py               # User login functionality
├── main.py                # Entry point for the application
├── models.py              # Database models definition
├── schemas.py             # Pydantic schemas for data validation
├── signup.py              # User registration logic
├── userdashboard.py       # User interface logic
├── __pycache__/           # Compiled Python files
└── README.md              # Project documentation

```

## 🔧 Installation and Setup

1. **Clone the Repository**
    ```sh
    git clone https://github.com/meeravali19/Banking_System_using_Python_FastAPI_Streamlit.git
    cd Banking_System_using_Python_FastAPI_Streamlit
    ```
2. **Create a Virtual Environment**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
    ```
4. **Run the Application**
   ```sh
   streamlit run main.py
    ```
Access the application at http://localhost:8501 in your web browser.

## 🖼️ Screenshots
![]()
## 🎥 Demo
A live demonstration of the application
 [🔗 Watch the Demo Video](https://drive.google.com/file/d/1K_sOnOYNt4lQkzxHjZMBy0xhV6XPJfN6/view?usp=sharing)
## 📌 Future Enhancements

Implement transaction history with filtering options.​
Add support for fund transfers between accounts.​
Integrate email notifications for account activities.​
Enhance security measures with two-factor authentication.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## ​📄 License

This project is open-source and available under the MIT License.

