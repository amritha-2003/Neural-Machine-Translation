import tkinter as tk
import subprocess

class TranslationApp:
    def __init__(self):
        self.init_gui()

    def init_gui(self):
        self.root = tk.Tk()
        self.root.title("Translation App")

        # Input text field
        self.input_text = tk.Entry(self.root, width=50)
        self.input_text.pack()

        # Submit button
        self.submit_button = tk.Button(self.root, text="Translate", command=self.on_submit)
        self.submit_button.pack()

        # Output text area
        self.output_text = tk.Text(self.root, width=50, height=10)
        self.output_text.pack()

        self.root.mainloop()

    def on_submit(self):
        input_text = self.input_text.get()
        if input_text:
            # Write input text to src-test.txt with utf-8 encoding
            with open("example.txt", "w", encoding="utf-8") as f:
                f.write(input_text)
            # Run translation command
            command = "onmt_translate -model run/model_step_30000.pt -src example.txt -output pred_1000.txt -gpu 0 -verbose"
            try:
                subprocess.run(command, shell=True, check=True)
                # Read output from pred_1000.txt with utf-8 encoding and display
                with open("pred_1000.txt", "r", encoding="utf-8") as f:
                    output = f.read()
            except Exception as e:
                output = str(e)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, output)
        else:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, "Please enter text to translate.")

if __name__ == "__main__":
    app = TranslationApp()
