
# Metaphrase

A simple command line applilcaition for translating languages using `ISO-639-1 Codes`

To view the list of supported languages, check `https://cloud.google.com/translate/docs/languages`


## Run Locally

Clone the project

```bash
  git clone https://github.com/mainaksamuel/metaphrase.git
```

Go to the project directory

```bash
  cd metaphrase
```

Install `metaphrase`

```bash
  python setup.py install
```


## Usage/Examples

Use the `ISO-639-1` language codes for setting the source `--sl` and target `--tl` languages.

---
\
Getting help

```bash
  metaphrase --help               # general help
  metaphrase translate --help     # help with translating texts
```
\
Setting the target language using the `--tl` flag
```bash
  metaphrase translate --tl=de --text="How are you?"
```

\
Setting source language using the `--sl` flag
```bash
  metaphrase translate --sl=en --tl=es --text="How was your day?"
```

\
Getting `text` and `target language` prompts.
```bash
  $ metaphrase translate ↵
  Enter text to translate: Howdy ↵
  Enter the target language ISO-639-1 Code to translate to: fr ↵
```

## License

[MIT](https://choosealicense.com/licenses/mit/)


