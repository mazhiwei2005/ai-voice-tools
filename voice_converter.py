"""
AI Voice Converter - Auto convert text or audio to character voice
Supports: GPT-SoVITS (TTS) + RVC (Voice Conversion)
"""

import os
import sys
import json
import shutil
import subprocess
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import time

# Paths
BASE_DIR = r"D:\stdio"
GPT_SOVITS_DIR = os.path.join(BASE_DIR, "GPT-SoVITS-Complete", "GPT-SoVITS-v3lora-20250228")
RVC_DIR = os.path.join(BASE_DIR, "RVC")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

# Create output dir
os.makedirs(OUTPUT_DIR, exist_ok=True)

class VoiceConverterApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AI Voice Converter")
        self.root.geometry("800x600")
        self.root.configure(bg="#1e1e2e")
        
        # Style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='#1e1e2e')
        self.style.configure('TLabel', background='#1e1e2e', foreground='#cdd6f4')
        self.style.configure('TButton', background='#313244', foreground='#cdd6f4')
        self.style.configure('TEntry', fieldbackground='#313244', foreground='#cdd6f4')
        
        self.setup_ui()
        self.check_services()
        
    def setup_ui(self):
        # Main frame
        main = ttk.Frame(self.root)
        main.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        ttk.Label(main, text="🎭 AI Voice Converter", font=("Arial", 20, "bold")).pack(pady=10)
        ttk.Label(main, text="Text to Speech + Voice Conversion", font=("Arial", 12)).pack()
        
        # Mode selection
        mode_frame = ttk.LabelFrame(main, text="Mode", padding=10)
        mode_frame.pack(fill=tk.X, pady=10)
        
        self.mode_var = tk.StringVar(value="text")
        ttk.Radiobutton(mode_frame, text="📝 Text → Voice", variable=self.mode_var, value="text").pack(side=tk.LEFT, padx=20)
        ttk.Radiobutton(mode_frame, text="🎵 Audio → Voice", variable=self.mode_var, value="audio").pack(side=tk.LEFT, padx=20)
        
        # Character selection
        char_frame = ttk.LabelFrame(main, text="Character Voice", padding=10)
        char_frame.pack(fill=tk.X, pady=10)
        
        self.char_var = tk.StringVar()
        chars = [
            "Raiden Shogun (雷电将军)",
            "Hu Tao (胡桃)",
            "Ganyu (甘雨)",
            "Nahida (纳西妲)",
            "Ayaka (神里绫华)",
            "Special Week (特别周)",
            "Silence Suzuka (无声铃鹿)",
            "Tokai Teio (东海帝王)",
            "Custom (自定义模型)"
        ]
        self.char_combo = ttk.Combobox(char_frame, textvariable=self.char_var, values=chars, state='readonly')
        self.char_combo.pack(fill=tk.X, padx=10)
        self.char_combo.set(chars[0])
        
        # Model path (for custom)
        model_frame = ttk.LabelFrame(main, text="Custom Model Path (if Custom selected)", padding=10)
        model_frame.pack(fill=tk.X, pady=5)
        
        self.model_path_var = tk.StringVar()
        ttk.Entry(model_frame, textvariable=self.model_path_var).pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Button(model_frame, text="Browse", command=self.browse_model).pack(side=tk.LEFT, padx=5)
        
        # Input frame
        input_frame = ttk.LabelFrame(main, text="Input", padding=10)
        input_frame.pack(fill=tk.X, pady=10)
        
        # Text input
        self.text_frame = ttk.Frame(input_frame)
        self.text_frame.pack(fill=tk.X)
        ttk.Label(self.text_frame, text="Text:").pack(anchor=tk.W)
        self.text_input = tk.Text(self.text_frame, height=4, bg="#313244", fg="#cdd6f4")
        self.text_input.pack(fill=tk.X, pady=5)
        
        # Audio input
        self.audio_frame = ttk.Frame(input_frame)
        ttk.Label(self.audio_frame, text="Audio File:").pack(anchor=tk.W)
        self.audio_path_var = tk.StringVar()
        ttk.Entry(self.audio_frame, textvariable=self.audio_path_var).pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Button(self.audio_frame, text="Browse", command=self.browse_audio).pack(side=tk.LEFT, padx=5)
        
        # Convert button
        btn_frame = ttk.Frame(main)
        btn_frame.pack(fill=tk.X, pady=20)
        
        self.convert_btn = ttk.Button(btn_frame, text="🚀 Convert", command=self.start_convert)
        self.convert_btn.pack(side=tk.LEFT, padx=10)
        
        ttk.Button(btn_frame, text="📁 Open Output", command=self.open_output).pack(side=tk.LEFT)
        
        # Progress
        self.progress = ttk.Progressbar(main, mode='indeterminate')
        self.progress.pack(fill=tk.X, pady=10)
        
        # Log
        log_frame = ttk.LabelFrame(main, text="Log", padding=10)
        log_frame.pack(fill=tk.BOTH, expand=True)
        
        self.log_text = tk.Text(log_frame, height=8, bg="#313244", fg="#a6e3a1")
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
        # Update UI based on mode
        self.mode_var.trace_add('write', self.update_mode)
        self.update_mode()
        
    def update_mode(self, *args):
        if self.mode_var.get() == "text":
            self.audio_frame.pack_forget()
            self.text_frame.pack(fill=tk.X)
        else:
            self.text_frame.pack_forget()
            self.audio_frame.pack(fill=tk.X)
    
    def browse_model(self):
        path = filedialog.askopenfilename(filetypes=[("Model", "*.pth")])
        if path:
            self.model_path_var.set(path)
    
    def browse_audio(self):
        path = filedialog.askopenfilename(filetypes=[("Audio", "*.mp3 *.wav *.flac *.ogg")])
        if path:
            self.audio_path_var.set(path)
    
    def open_output(self):
        os.startfile(OUTPUT_DIR)
    
    def log(self, msg):
        self.log_text.insert(tk.END, f"{msg}\n")
        self.log_text.see(tk.END)
        self.root.update()
    
    def check_services(self):
        """Check if GPT-SoVITS and RVC are running"""
        self.log("🔍 Checking services...")
        
        # Check GPT-SoVITS
        try:
            import requests
            r = requests.get("http://127.0.0.1:9874", timeout=2)
            self.log("✅ GPT-SoVITS is running")
        except:
            self.log("⚠️ GPT-SoVITS not running (start Start_GPT-SoVITS-Complete.bat)")
        
        # Check RVC
        try:
            r = requests.get("http://127.0.0.1:7897", timeout=2)
            self.log("✅ RVC is running")
        except:
            self.log("⚠️ RVC not running (start Start_RVC_Web.bat)")
    
    def get_model_path(self):
        """Get the RVC model path based on character selection"""
        char = self.char_var.get()
        
        if "Custom" in char:
            return self.model_path_var.get()
        
        # Map character names to model files
        model_map = {
            "Raiden Shogun": "raiden_shogun.pth",
            "Hu Tao": "hu_tao.pth",
            "Ganyu": "ganyu.pth",
            "Nahida": "nahida.pth",
            "Ayaka": "ayaka.pth",
            "Special Week": "special_week.pth",
            "Silence Suzuka": "silence_suzuka.pth",
            "Tokai Teio": "tokai_teio.pth"
        }
        
        for key, val in model_map.items():
            if key in char:
                model_path = os.path.join(RVC_DIR, "assets", "weights", val)
                if os.path.exists(model_path):
                    return model_path
                else:
                    self.log(f"❌ Model not found: {model_path}")
                    self.log(f"📥 Please download from Hugging Face first")
                    return None
        
        return None
    
    def convert_text_to_voice(self, text, model_path):
        """Convert text to voice using GPT-SoVITS + RVC"""
        self.log(f"📝 Converting text: {text[:50]}...")
        
        # Step 1: Use GPT-SoVITS for TTS
        tts_output = os.path.join(OUTPUT_DIR, "tts_output.wav")
        
        try:
            # Call GPT-SoVITS API
            import requests
            
            self.log("🎤 Calling GPT-SoVITS TTS...")
            response = requests.post(
                "http://127.0.0.1:9874/tts",
                json={
                    "text": text,
                    "text_language": "zh"
                },
                timeout=60
            )
            
            if response.status_code == 200:
                with open(tts_output, 'wb') as f:
                    f.write(response.content)
                self.log(f"✅ TTS completed: {tts_output}")
            else:
                self.log(f"❌ TTS failed: {response.status_code}")
                return None
                
        except Exception as e:
            self.log(f"❌ TTS error: {e}")
            return None
        
        # Step 2: Use RVC for voice conversion
        return self.convert_audio_voice(tts_output, model_path)
    
    def convert_audio_voice(self, audio_path, model_path):
        """Convert audio using RVC"""
        self.log(f"🎵 Converting audio with RVC...")
        
        output_path = os.path.join(OUTPUT_DIR, f"converted_{int(time.time())}.wav")
        
        try:
            # Call RVC API
            import requests
            
            with open(audio_path, 'rb') as f:
                response = requests.post(
                    "http://127.0.0.1:7897/voice2voice",
                    files={"audio": f},
                    data={
                        "model_path": model_path,
                        "f0_up_key": 0,
                        "f0_method": "rmvpe",
                        "index_rate": 0.5,
                        "filter_radius": 3,
                        "resample_sr": 0,
                        "volume_envelope": 0.25,
                        "protect": 0.33
                    },
                    timeout=120
                )
            
            if response.status_code == 200:
                with open(output_path, 'wb') as f:
                    f.write(response.content)
                self.log(f"✅ Voice conversion completed: {output_path}")
                return output_path
            else:
                self.log(f"❌ RVC failed: {response.status_code}")
                return None
                
        except Exception as e:
            self.log(f"❌ RVC error: {e}")
            return None
    
    def start_convert(self):
        """Start conversion in a separate thread"""
        self.convert_btn.config(state='disabled')
        self.progress.start()
        
        thread = threading.Thread(target=self.do_convert)
        thread.daemon = True
        thread.start()
    
    def do_convert(self):
        """Do the actual conversion"""
        try:
            model_path = self.get_model_path()
            if not model_path:
                self.log("❌ No model selected")
                return
            
            if self.mode_var.get() == "text":
                text = self.text_input.get("1.0", tk.END).strip()
                if not text:
                    self.log("❌ No text entered")
                    return
                result = self.convert_text_to_voice(text, model_path)
            else:
                audio_path = self.audio_path_var.get()
                if not audio_path or not os.path.exists(audio_path):
                    self.log("❌ No audio file selected")
                    return
                result = self.convert_audio_voice(audio_path, model_path)
            
            if result:
                self.log(f"\n🎉 Done! Output: {result}")
                # Auto play
                os.startfile(result)
            else:
                self.log("\n❌ Conversion failed")
                
        except Exception as e:
            self.log(f"❌ Error: {e}")
        finally:
            self.progress.stop()
            self.convert_btn.config(state='normal')
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = VoiceConverterApp()
    app.run()
