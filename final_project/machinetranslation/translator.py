"""
Module for translation functions using MyMemoryTranslator.
"""

from deep_translator import MyMemoryTranslator

translator = MyMemoryTranslator(source='en', target='fr')

def translate_english_to_french(english_text):
    """
    Translates English text to French.
    """
    translation = translator.translate(english_text)
    return translation

def translate_french_to_english(french_text):
    """
    Translates French text to English.
    """
    translation = translator.translate(french_text, source='fr', target='en')
    return translation

def english_to_french(english_text):
    """
    Translates English text to French (alternative function name).
    """
    translation = translator.translate(english_text)
    return translation

def french_to_english(french_text):
    """
    Translates French text to English (alternative function name).
    """
    translation = translator.translate(french_text, source='fr', target='en')
    return translation
