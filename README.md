![Logo](./assets/logo.png)

# Ringerous

Simple, minimal, and lightweight app to test some set for satisfying Ring properties.

## Features

You can test for modulo integers with our "Modulo Integer Mode".

You can set up custom binary operations with our "Custom Binary Table Mode".

You can also process a batch by loading files and export the result as CSV with our "Batch Process Mode".

## Who wrote this crap

[Lawrance Cancerlon](https://github.com/Lawrance-Cancerlon)
[Ananda Risyad](https://github.com/Wakugumi)
[Yonathan Henry Christianto](https://github.com/henrychristianto)
[Bryan Wu](https://github.com/BryanWu1020)

## Why

It's an assessment on our Ring theory class.

# Installation

## Download executables from Release

In our GitHub release, you can find our published binary executables which you can directly run in your system. Download the executables according to your system

```bash
Ringerous-<VERSION_NUMBER>.exe # Windows
Ringerous-<VERSION_NUMBER>.AppImage # Linux (AppImage)
```

## Run with Python

We assume you are running Windows and has set up Python correctly. This program runs on Python version 3.x.

Download the source code from the release page or by cloning this repository:

```bash
git clone https://github.com/Lawrance-Cancerlon/Ringerous.git
```

Then go inside the directory of the repository or the extracted files (if downloaded from the Release as ZIP).

Next, install the python libraries from `requirements.txt`:

```bash
pip install -r requirements.txt
```

It should run smoothly if there are no problem with your installed Python.

After that, you can run the app by running this command:

```bash
python app.py

# or some machine should run python like this
python3 app.py
```

# How to use this

![Figure 1 - User Interface of the program.](./assets/figure_1.png)

In the figure above is our app's user interface, the first thing you'll see when launch. The app will look like it throughout any kind of task use on it.
The left pane which has white background is the output message pane. Any error log or result will display on it.
The right panel is the operations panel. There are three tabs which navigate to the available modes to use.

## Modulo Integer mode

In this mode, you'll see a large Z letter which state that we are doing a set of integers with modulo. When you enter the modulo number, the label adjust accordingly.
To run the checker, click the `Enter` button to run. If the aforementioned set satisfies Ring property, there should be 6 checkmarks. Otherwise the corresponding error of each properties is displayed alongside its counterexample (if exists).

## Custom Binary Table mode

In the `Elements` input field, you get to input your set's elements. The matrix entries size will adjust accordingly when you edit your elements. Make sure to follow the format accordingly.

```bash
1, 2, 3 # use comma as the seperator
```

![Figure 2 - Testing for an invalid ring.](./assets/figure_2.png)

## Batch Process mode

In this mode, you get to select multiple files from your directory. If each file is not in our acceptable format, the program won't display any result.

We only accept JSON file in the following format:

```JSON
{
  "elements" : ['a', 'b'],

  "add_table" : [
    ['a', 'a'], ['b, 'b']
  ],
  "mul_table" : [
    ['a', 'a'], ['b, 'b']
  ]
}
```

where 'a' and 'b' can be in integer too (without the quotes).

Once they are processed, the display pane will print out which files is loaded and passed. Then you can export to your prefered directory and filename.
The export file will be given an ".csv" extension.

# Note

In the app, you can either validate an cyclic group of integers module _n_, where you can enter _n_ in the input box.
You can also test your own set by using in the "tests" folder, in there you'll find example in JSON files.
You can upload batches of JSON file to be validated.
You can Export the result in CSV file.

# Contribute

Go ahead make something useful tho.
