import base64
import argparse
import urllib.parse

def encode_base64(s):
    return base64.b64encode(s.encode()).decode()
def decode_base64(s):
    return base64.b64decode(s).decode()

def encode_url(s):
    return urllib.parse.quote(s)
def decode_url(s):
    return urllib.parse.unquote(s)

def encode_hex(s):
    return s.encode().hex()
def decode_hex(s):
    return bytes.fromhex(s).decode()

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
            decoded_string = decode_url(args.string)
            print(decoded_string)
        else:
            encoded_string = encode_url(args.string)
            print(encoded_string)
    elif args.f == 'hex':
        if args.d:
            decoded_string = decode_hex(args.string)
            print(decoded_string)
        else:
            encoded_string = encode_hex(args.string)
            print(encoded_string)
    else:
        print(f"Unsupported format: {args.f}")

if __name__ == '__main__':
    main()