#!/usr/bin/env python3
import click
from metaphrase.app import get_translation


@click.group()
@click.version_option("1.0.0")
def main():
    """A CLI Language translation app."""
    click.echo("""
    Refer to `https://cloud.google.com/translate/docs/languages`
            for acceptable ISO-639-1 Language Codes
    """)


@main.command()
@click.option('--text', prompt='Enter text to translate',
              help='Text to translate')
@click.option('--sl', default='auto',
              help='Optional source language (ISO-639-1 Code) to translate from (defaults to `auto`).')
@click.option('--tl', help='Target language (ISO-639-1 Code) to translate to.',
              prompt='Enter the target language ISO-639-1 Code to translate to')
def translate(sl, tl, text):
    """
    Translate from one language to another.
    This requires that you specify the text to translate and target language to
    translate to.
    """
    click.echo(get_translation(sl, tl, text))


if __name__=="__main__":
    main()
