from flask import Flask, render_template, request
from scanner import PortScanner

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    open_ports = None
    if request.method == "POST":
        ip = request.form.get("ip")
        start_port = int(request.form.get("start_port"))
        end_port = int(request.form.get("end_port"))

        # Cria o scanner e realiza o scan
        scanner = PortScanner(ip, start_port, end_port)
        open_ports = scanner.scan()

    return render_template("index.html", open_ports=open_ports)


if __name__ == "__main__":
    app.run(debug=True)
