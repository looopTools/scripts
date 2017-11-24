import argparse
from config import Config

def main():
    parser = argparse.ArgumentParser(description='Parse config file')
    parser.add_argument('config', help='define configuration file')
    args = parser.parse_args()
    config = Config.build(args.config)
    print('site: {} interval: {}'.format(config.site, config.interval))

if __name__ == "__main__":
    main()
