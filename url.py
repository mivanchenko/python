import urllib.request
import json
import yaml

def main():
    with open('list.yml') as fh:
        redirects = yaml.load(fh)

    for redirect in redirects:
        uri, redirect_to = redirect['original'], redirect['redirect']
        request = urllib.request.Request(
            f'https://url.com/?url={uri}',
            headers={'X-Token': '<token goes here>'}
        )
#        with urllib.request.urlopen(request) as resp:
#            data = json.load(resp)

        if data['status'] != 'redirect':
            print(f'Missing redirect: {uri}: status - {data["status"]}')
        elif data['redirect_to'] != redirect_to:
            print(f'Invalid redirect: {uri} should redirect to {data["redirect_to"]}')

if __name__ == '__main__':
    main()
