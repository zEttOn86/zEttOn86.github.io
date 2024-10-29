from factory_method import create_beer

def main():
    asahi = create_beer("asahi_beer")
    sapporo = create_beer("sapporo_beer")

if __name__ =="__main__":
    main()