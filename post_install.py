import os
from pathlib import Path
import configparser

def prompt_aws_credentials():
    access_key = input('Enter AWS Access Key ID: ')
    secret_key = input('Enter AWS Secret Access Key: ')
    region = input('Enter AWS Region: ')

    aws_credentials = {
        'AWS_ACCESS_KEY_ID': access_key,
        'AWS_SECRET_ACCESS_KEY': secret_key,
        'AWS_REGION': region
    }

    config = configparser.ConfigParser()
    config['default'] = aws_credentials

    config_path = Path.home() / '.aws' / 'credentials'
    config_path.parent.mkdir(parents=True, exist_ok=True)

    with open(config_path, 'w') as configfile:
        config.write(configfile)
    
    print(f"AWS credentials saved to {config_path}")

if __name__ == "__main__":
    prompt_aws_credentials()
