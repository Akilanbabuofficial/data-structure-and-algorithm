def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from source {source} to destination {destination}")
        return
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from source {source} to destination {destination}")
    TowerOfHanoi(n - 1, auxiliary, destination, source)
n = int(input("enter the number:"))
TowerOfHanoi(n, 'A', 'B', 'C')
