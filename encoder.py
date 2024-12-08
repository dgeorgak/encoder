import base64
import argparse
import urllib.parse

def encode_base64(s):
    return base64.b64encode(s.encode()).decode()
def decode_base64(s):
    return base64.b64decode(s).decode()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f')
    parser.add_argument('string')
    parser.add_argument('-d', action='store_true')
    args = parser.parse_args()

    if args.f == 'base64':
        if args.d:
            decoded_string = decode_base64(args.string)
            print(decoded_string)
        else:
            encoded_string = encode_base64(args.string)
            print(encoded_string)
    elif args.f == 'url':
        if args.d:
            decoded_string = urllib.parse.unquote(args.string)
            print(decoded_string)
        else:
            encoded_string = urllib.parse.quote(args.string)
            print(encoded_string)
    else:
        print(f"Unsupported format: {args.f}")

if __name__ == '__main__':
    main()