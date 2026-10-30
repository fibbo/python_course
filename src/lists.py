# Do not run this line!
# print(list(range(1000000000000)))


queue = ["a.pdf", "b.pdf", "c.pdf", "d.pdf", "e.pdf", "f.pdf"]


if __name__ == "__main__":
    print(queue[::3])

    queue.append("g.pdf")

    print(queue)

    print(queue[::3])

    t = (3, 5)

    print(t)
