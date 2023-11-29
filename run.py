import sys
if len(sys.argv) == 2:
    if sys.maxsize > 2*32:
        file = sys.argv[1]
        import Bypass
        Bypass.Bypass(file)
    else:
        print("YOUR SYSTEM IS 32bit")
        sys.exit()
