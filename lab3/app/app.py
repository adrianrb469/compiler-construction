from flask import Flask, request, jsonify
import subprocess
import os
import tempfile

app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to the MiniLang Compiler Service!"


@app.route("/compile", methods=["POST"])
def compile_code():
    # Get the code from the request
    code = request.json.get("code")
    if not code:
        return jsonify({"error": "No code provided"}), 400

    # Create a temporary file to store the code
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False
    ) as temp_file:
        temp_file.write(code)
        temp_file_path = temp_file.name

    try:
        # Run ANTLR command with visitor generation
        antlr_command = (
            f"antlr -Dlanguage=Python3 -visitor -no-listener /program/MiniLang.g4"
        )
        subprocess.run(antlr_command, shell=True, check=True)

        # Run the Driver
        driver_command = f"python3 /program/Driver.py {temp_file_path}"
        result = subprocess.run(
            driver_command, shell=True, capture_output=True, text=True, check=True
        )

        # Return the output
        return jsonify({"output": result.stdout, "errors": result.stderr})

    except subprocess.CalledProcessError as e:
        return (
            jsonify(
                {"error": "Compilation failed", "output": e.stdout, "errors": e.stderr}
            ),
            500,
        )

    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
