# PromptoExperimentation

[![Prompto - Demo Video.jpg](Prompto%20-%20Demo%20Video.jpg)](https://youtu.be/95AEFzuPio0)

Demo Showcase: https://youtu.be/95AEFzuPio0

## Abstract

300 words

## Requirements

Python Version >= 3.9

## Getting Started

1. Clone this repository.
2. Create a virtual environment: `python3 -m venv .venv`
3. Activate the virtual environment: `source .venv/bin/activate`
4. Install requirements: `pip install -r requirements.txt`
5. Create a `.env`-File with an OpenAI key exposed like this: `OPENAI_API_KEY=<YOUR OPENAI KEY>`
6. To start the chatbot run: `streamlit run main.py`

## Folder Structure

### Examples

Contains two files for a chat example with LangServe building a simple chatbot based on Pronto Documentation.

Simply run

```
python3 examples/server.py
```

### Notebooks

The notebooks in this folder served as experimentation for fine-tuning the RAG.

### Pronto-Docs

Auto-generated documentation from all Pronto Behaviors in Markdown.

#### Generating pronto documentation

https://github.com/GDQuest/gdscript-docs-maker

I used this tool to first build a reference json file and generate afterward markdown files of each behavior.

I had a couple of problems with the tool:
1. The automated generate reference shell script didn't work for me. For some reason the Editor just crashed.
2. A workaround included importing the required GDScripts directly into Godot and let it generate from the Editor. One additional step I had to take was to specify only the directory with behavior classes (res://addons/pronto/behavior) as one or two directory levels higher crashed the editor (also happened in a different Godot project).
3. For the actual markdown generation a Python module called gdscript_docs_maker is used. For some reason trying to use the module directly didn't work, but calling the `__main__` script with it does. I created an issue on GitHub for this: https://github.com/GDQuest/gdscript-docs-maker/issues/94

The resulting markdown files are saved in the folder [pronto-docs](pronto-docs).