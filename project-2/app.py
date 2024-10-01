from flask import Flask, request, jsonify
import subprocess
import tempfile
import os
import sys

sys.path.append("/program")

from Driver import compilador

app = Flask(__name__)


@app.route("/compile", methods=["POST"])
def compile_code():
    code = request.json.get("code")
    if not code:
        return jsonify({"error": "No code provided"}), 400

    try:
        # Run ANTLR command with visitor generation
        antlr_command = (
            f"antlr -Dlanguage=Python3 -visitor -no-listener /program/Compiscript.g4"
        )
        subprocess.run(antlr_command, shell=True, check=True)

        # Use compilador function directly
        result = compilador(code)

        if result == 1:
            return jsonify({"error": "Compilation failed"}), 500

        # If compilation was successful, result contains the parse tree
        return jsonify(
            {
                "output": result,
                "message": "Compilation successful. Check ./output/graph.png for the AST visualization.",
            }
        )

    except subprocess.CalledProcessError as e:
        return (
            jsonify(
                {
                    "error": "ANTLR command failed",
                    "output": e.stdout,
                    "errors": e.stderr,
                }
            ),
            500,
        )
    except Exception as e:
        return jsonify({"error": "Compilation failed", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
