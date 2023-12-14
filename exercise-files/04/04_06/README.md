## Create a virtual environment :

```
python -m venv env
```

## Activate the virtual environment :

```
source env/bin/activate
```

## [get an key](https://platform.openai.com/account/api-keys)

`export OPENAI_API_KEY=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`

## Installation:

### install requirements :

use `pip3 on a mac`
`pip install -r requirements.txt`

### install whisper model - (openai-whisper)[https://pypi.org/project/openai-whisper/]

`pip install git+https://github.com/openai/whisper.git`

[README](https://github.com/openai/whisper)

`pip install -U openai-whisper`

### install ffmpeg (requirements for the whisper library)

#### On macOS:

`brew install ffmpeg`

#### On Ubuntu:

```
sudo apt update
sudo apt install ffmpeg

```

#### On Windows:

Download the executable from the [official FFmpeg site](https://ffmpeg.org/download.html)

## Start the app:

`streamlit run main.py`
