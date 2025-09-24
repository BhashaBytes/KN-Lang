import subprocess

mapping = {
    "ಮುದ್ರಿಸು": "print", "mudrisu": "print",
    "ಒಳತೆಗೆಯು": "input", "olategayu": "input",
    "ಒಂದೇ": "if", "onde": "if",
    "ಅಥವಾ_ಒಂದೇ": "elif", "athava_onde": "elif",
    "ಅಥವಾ": "else", "athava": "else",
    "ಗಾಗಿ": "for", "gaagi": "for",
    "ವರೆಗೆ": "while", "varege": "while",
    "ವಿವರಣೆ": "def", "vivarane": "def",
    "ವರ್ಗ": "class", "varga": "class",
    "ಮರಳಿ": "return", "marali": "return",
    "ಮುರಿ": "break", "muri": "break",
    "ಮುಂದುವರಿಸು": "continue", "munduvarisu": "continue",
    "ಆಮದು": "import", "aamadu": "import",
    "ಇಂದ": "from", "inda": "from",
    "ಹೆಸರಿನಲ್ಲಿ": "as", "hesarinalli": "as",
    "ಜೊತೆಗೆ": "with", "joteghe": "with",
    "ಪ್ರಯತ್ನಿಸು": "try", "prayatnisu": "try",
    "ವ್ಯತ್ಯಾಸ": "except", "vyatyaasa": "except",
    "ಕೊನೆಯಲ್ಲಿ": "finally", "koneyalli": "finally",
    "ಸತ್ಯ": "True", "satya": "True",
    "ಸುಳ್ಳು": "False", "sullu": "False",
    "ಶೂನ್ಯ": "None", "shoonya": "None",
    "ಅಥವಾ_": "or", "athava_": "or"
}

def translate(code: str) -> str:
    for kn, eng in mapping.items():
        code = code.replace(kn, eng)
    return code

def run_knlang_file(filename="test.kn"):
    with open(filename, "r", encoding="utf-8") as f:
        kn_code = f.read()
    python_code = translate(kn_code)
    with open("temp.py", "w", encoding="utf-8") as f:
        f.write(python_code)
    subprocess.run(["python3", "temp.py"])

if __name__ == "__main__":
    run_knlang_file()
