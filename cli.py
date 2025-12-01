import argparse

v="1.0"

def main():
    p=argparse.ArgumentParser(description="cli tool sederhana")
    s=p.add_subparsers(dest="c")

    h=s.add_parser("hello")
    h.add_argument("-n","--name")

    a=s.add_parser("add")
    a.add_argument("x")
    a.add_argument("y")

    s.add_parser("ver")

    args=p.parse_args()

    if args.c=="hello":
        print("Hello", args.name if args.name else "User")
    elif args.c=="add":
        try:
            print(int(args.x)+int(args.y))
        except:
            print("error angka")
    elif args.c=="ver":
        print(v)
    else:
        p.print_help()

if __name__=="__main__":
    main()
