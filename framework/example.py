from gooey.python_bindings.gooey_decorator import Gooey
from gooey.python_bindings.gooey_parser import GooeyParser

@Gooey
def main():
    parser = GooeyParser(description='Example validator')
    parser.add_argument(
        'secret',
        metavar='Super Secret Number',
        help='A number specifically between 2 and 14',
        gooey_options={
            'validator': {
                'test': '2 <= int(user_input) <= 14',
                'message': 'Must be between 2 and 14'
            }
        })

    args = parser.parse_args()

    print("Cool! Your secret number is: ", args.secret)


if __name__ == '__main__':
    main()
