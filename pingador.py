import random
import subprocess

adresses = {
        1 : "10.0.0.21",
        2 : "10.0.0.31",
        3 : "10.0.0.33",
        4 : "10.0.0.41",
        5 : "10.0.0.42",
} 

# valores definidos para que os tres computadores que simulam o fluxo normal enviem cerca de 100000 pacotes
n_packets = 271
n_turns = 123

def main():
    for i in range(n_turns):
        server = random.randint(1,6)
        subprocess.call(["sudo", "ping", "-i 0.1", "-c {}".format(n_packets), adresses[server]])

if __name__ == '__main__':
    main()
