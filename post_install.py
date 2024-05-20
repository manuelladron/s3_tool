import os
from pathlib import Path
import configparser

def prompt_aws_credentials():
    config = configparser.ConfigParser()
    config_path = Path.home() / '.aws' / 'credentials'
    
    # Load existing credentials if they exist
    if config_path.exists():
        config.read(config_path)

    if 'default' not in config:
        config['default'] = {}

    ak_existed = True
    sk_existed = True
    region_existed = True
    
    # Check if each credential exists and prompt if missing
    access_key = config['default'].get('aws_access_key_id')
    if not access_key:
        access_key = input('Enter AWS Access Key ID: ')
        ak_existed = False

    secret_key = config['default'].get('aws_secret_access_key')
    if not secret_key:
        secret_key = input('Enter AWS Secret Access Key: ')
        sk_existed = False

    region = config['default'].get('region')
    if not region:
        region = input('Enter AWS Region: ')
        region_existed = False

    # Only update the credentials that were missing
    if not config['default'].get('aws_access_key_id') and not ak_existed:
        config['default']['aws_access_key_id'] = access_key
    if not config['default'].get('aws_secret_access_key') and not sk_existed:
        config['default']['aws_secret_access_key'] = secret_key
    if not config['default'].get('region') and not region_existed:
        config['default']['region'] = region


    # Ensure .aws directory exists
    config_path.parent.mkdir(parents=True, exist_ok=True)

    # Write the updated config to the credentials file
    if not ak_existed or not sk_existed or not region_existed:
        with open(config_path, 'w') as configfile:
            config.write(configfile)

        print(f"AWS credentials saved to {config_path}")

if __name__ == "__main__":
    prompt_aws_credentials()
