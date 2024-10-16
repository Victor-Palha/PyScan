# Port Scanner

A simple and efficient **Port Scanner** built with Python and Flask, designed to identify open ports on a given IP address. This mini project serves as a practical demonstration of network security concepts and the basics of web development with Flask.

## Features

- **Scan Ports**: Check for open ports on any specified IP address.
- **Web Interface**: User-friendly web interface to input parameters and view results.
- **Service Identification**: Identifies common services running on the open ports.

## Tech Stack

- **Python**: The programming language used for the application logic.
- **Flask**: A lightweight web framework for building the web interface.
- **Socket**: Python's built-in library for network connections.

## Installation

To get started with the Port Scanner, follow these steps:

### Prerequisites

Make sure you have Python 3.0.3 installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository

```bash
git clone https://github.com/victor-palha/PyScan.git
cd port-scanner
```

### Install Flask

You can install Flask using pip:

```bash
pip install flask
```

## Usage

1. **Run the Application**:

   In the terminal, navigate to the project directory and run:

   ```bash
   python main.py
   ```

2. **Access the Web Interface**:

   Open your web browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).

3. **Input Parameters**:

   - Enter the IP address you want to scan.
   - Specify the starting and ending ports for the scan.
   - Click on the **Scan** button.

4. **View Results**:

   The application will display the open ports found during the scan.

## Code Structure

```
port-scanner/
├── scanner.py       # Contains the PortScanner class for scanning logic
├── main.py           # Flask application for the web interface
└── templates/
    └── index.html   # HTML template for the main page
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or features, feel free to open an issue or submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

## Acknowledgments

- Inspired by the concepts of network security and ethical hacking.
- Thanks to the Flask documentation for guidance on web development.

## Contact

For inquiries or questions, feel free to reach out:

- **Email**: jv.palha@gmail.com
- **GitHub**: [Victor Palha](https://github.com/victor-palha)

---

Happy scanning!
