from boto3 import Session

VOICES_DICT = {
    "Female (US)": "Joanna",
    "Male (US)": "Matthew",
    "Female (US child)": "Ivy",
    "Male (US child)": "Justin",
    "Female (British)": "Amy",
    "Male (British": "Brian",
}


class Audio:
    def __init__(self):
        self.voice_key = ""

    # Uses AWS "polly" to convert the string of text into an MP3 audio file
    def create_mp3(self, text, path):
        polly_client = Session(profile_name="shibarak").client('polly')
        response = polly_client.synthesize_speech(
            VoiceId=VOICES_DICT[self.voice_key],
            OutputFormat='mp3',
            Text=text,
            Engine='neural')

        with open(path, 'wb') as file:
            file.write(response['AudioStream'].read())
            file.close()
