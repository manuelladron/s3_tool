import os
from pathlib import Path
import configparser

def prompt_aws_credentials():
    config = configparser.ConfigParser()
    config_path = Path.home() / '.aws' / 'credentials'
    
    if not config_path.exists():
        config_path.parent.mkdir(parents=True, exist_ok=True)

    config.read(config_path)

    if 'default' not in config:
        config['default'] = {}

    access_key = input('Enter AWS Access Key ID: ')
    secret_key = input('Enter AWS Secret Access Key: ')
    region = input('Enter AWS Region: ')

    config['default']['aws_access_key_id'] = access_key
    config['default']['aws_secret_access_key'] = secret_key
    config['default']['region'] = region

    with open(config_path, 'w') as configfile:
        config.write(configfile)

    print(f"AWS credentials saved to {config_path}")

if __name__ == "__main__":
    prompt_aws_credentials()
