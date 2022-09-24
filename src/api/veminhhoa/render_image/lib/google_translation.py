import six
from google.cloud import translate_v2 as translate
import json
from google.oauth2 import service_account
from pathlib import Path

ROOT_DIR = str(Path(__file__).resolve(strict=True).parent.parent.parent)


class PromptTranslation():
    @staticmethod 
    def translate_prompt(text, target='en'):
        """Translates text into the target language.

        Target must be an ISO 639-1 language code.
        See https://g.co/cloud/translate/v2/translate-reference#supported_languages
        """
        path =  ROOT_DIR + '/../config/google_cloud_credentials.json'
        credentials = service_account.Credentials.from_service_account_file(path)
        translate_client = translate.Client(credentials=credentials)

        result = translate_client.translate(text, target_language=target)

        return result['translatedText']
        # print(u"Text: {}".format(result["input"]))
        # print(u"Translation: {}".format(result["translatedText"]))
        # print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))

if __name__ == "__main__":
    print(PromptTranslation.translate_prompt(text="con gà gáy sáng trên vùng đồi núi Việt Nam"))
