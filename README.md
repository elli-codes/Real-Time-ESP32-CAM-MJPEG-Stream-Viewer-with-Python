# Real-Time-ESP32-CAM-MJPEG-Stream-Viewer-with-Python
A Python-based desktop application that receives and displays a live MJPEG video stream from an ESP32-CAM using HTTP and Tkinter.

This project focuses on understanding how an MJPEG stream is transmitted over HTTP and how individual JPEG frames can be extracted from a continuous byte stream.

📌 Overview

The ESP32-CAM continuously sends JPEG images as an MJPEG stream over HTTP.

Instead of treating the response as a single image, this project reads the incoming data in chunks, stores the received bytes in a buffer, identifies the HTTP/MJPEG frame header, reads the Content-Length, and extracts each JPEG frame individually.

The extracted frames are then converted into PIL images and displayed in a Tkinter window.
✨ Features:
📷 Live video streaming from ESP32-CAM
🌐 HTTP MJPEG stream reception
📦 Chunk-based data processing
🧠 Persistent byte buffer for incomplete frames
🔎 HTTP header detection using \r\n\r\n
📏 JPEG frame size detection using Content-Length
🖼️ JPEG extraction and decoding with Pillow
🖥️ Real-time display using Tkinter
🔄 Continuous frame processing without blocking the GUI
🛠️ Technologies:
Python 3
ESP32-CAM
Tkinter
Requests
Pillow
HTTP
MJPEG
Byte Streams / Buffer Processing

🖥️ Tkinter GUI:

The graphical user interface is built with Tkinter.

The GUI receives the extracted JPEG frames from the ESP32-CAM stream and displays them continuously in a Tkinter window.

The image processing pipeline is:

MJPEG Stream
     ↓
JPEG Frame
     ↓
BytesIO
     ↓
Pillow Image
     ↓
ImageTk.PhotoImage
     ↓
Tkinter Label

Tkinter's after() method is used to continuously process incoming data while keeping the GUI responsive.

📡 ESP32-CAM Configuration:

The ESP32-CAM configuration is provided in the .ino file by using Arduino IDE and libraries.

The .ino file contains the network configuration, including the Wi-Fi credentials and the camera's network settings.

After uploading the .ino code to the ESP32-CAM, the camera obtains an IP address on the network.

The Python application then connects to the camera's MJPEG stream using:

http://<ESP32-CAM-IP>:81/stream

For example:

http://192.168.137.60:81/stream

If the ESP32-CAM receives a different IP address, update the stream URL in the Python code accordingly.
