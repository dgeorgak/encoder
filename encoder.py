import base64
import argparse

def encode_base64(s):
    return base64.b64encode(s.encode()).decode()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f')
    parser.add_argument('string')
    args = parser.parse_args()

    if args.f == 'base64':
        encoded_string = encode_base64(args.string)
        print(encoded_string)
    else:
        print(f"Unsupported format: {args.f}")

if __name__ == '__main__':
    main()