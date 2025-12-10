# Auto plot generation from CSV and saving as JPEG images
Auto plot generation from CSV and saving as JPEG images / CSVから連続でグラフ作成しJpeg画像で保存\
This GitHub repository is based on my article originally published on Zenn.\
このGitHubリポジトリは私自身のZennの記事をもとに移載しています。\
Zenn URL: https://zenn.dev/eito_assy/articles/22184cddcc9ac4
\

# Overview
I created a Python program that automatically creates a series of simple graph images from CSV files in a folder.
As an example, I envision using this program for simple data checking of raw data in measuring equipment (electrical properties, etc.) in university laboratories (semiconductor devices, etc.).

# Background
In a semiconductor device laboratory, I sometimes struggled with compiling data after measuring electrical characteristics. Measurement data for each measurement point was output in CSV file format, and I had to manually create waveform graphs and check the data. Once I confirmed the optimal conditions that met the requirements, I manually performed a detailed analysis based on that data, but even just to make a simple judgment as to whether the data was optimal, I had to manually check each file, which was a simple and time-consuming task.
I created a Python program to create graph images from CSV files to make this simple judgment.
The purpose is to simply check the shape of the graph, not to perform a detailed analysis.
<img width="2612" height="926" alt="image" src="https://github.com/user-attachments/assets/5d24677e-7e2b-4d5b-8280-35bc2222870a" />
<img width="2884" height="729" alt="image" src="https://github.com/user-attachments/assets/3cb325b6-f9ce-45d1-9903-3d848e3f7902" />

# How to Use
Use Pyinstaller to create an EXE file from the above source code, place the EXE file in the folder containing the file you want to create a graph from, and run the EXE file.
When "COMPLETE!!" appears on the screen, all operations are complete. You can close the screen by clicking the X button.

# About graph image
The graph on the left shows a linear vertical axis, and the graph on the right shows a logarithmic vertical axis. Both horizontal axes are linear.
In the logarithmic notation, absolute values ​​are taken, negative values ​​are converted to positive values, and then a logarithmic conversion is performed.
For versatility, the axes are named x axis and y axis. Users are encouraged to change the names to suit their own needs.
<img width="748" height="435" alt="image" src="https://github.com/user-attachments/assets/e82762fe-78df-4544-87bf-085f690c55ca" />

Headers are taken from the first line of the CSV file. There is no limit to the number of headers.
The first line is used as the horizontal axis, and from the second line onwards it is used as the vertical axis. Any number of columns can be read and displayed on the graph.
<img width="2505" height="1187" alt="image" src="https://github.com/user-attachments/assets/6c9b9f31-55bb-4c5f-a2ea-e3277d3771d6" />

# Python Version
Python: 3.12.5
pandas version: 2.2.2
matplotlib version: 3.10.0
numpy version: 2.0.1
Pyinstaller: 6.12.0

# Impressions
In creating this program, I did not use AI tools like ChatGPT or Gemini, which have become commonplace recently. I coded everything myself.
(The graph images were randomly output by Gemini for reference.)
Also, since the author does not conduct research or work in programming, some parts may have been written in an unconventional way.
Looking back, I believe the main processing should have been written using __init__.py, which is a standard way of writing in Python.
Although not using AI took a considerable amount of time and effort, it was a valuable experience in terms of being able to solve problems on my own when I got stuck and understanding all the source code.
As for issues, there are some areas where I am not able to use the __init__.py specifications and class definitions mentioned above, but I would like to deepen my understanding in the future.

# Usage Notes
I hope that this code will be useful for research students experiencing similar problems to easily check the graph waveforms of CSV data.
The author assumes no responsibility for any problems that may arise when using this program.

