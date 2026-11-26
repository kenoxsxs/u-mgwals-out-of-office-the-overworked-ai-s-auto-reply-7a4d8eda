"""Write one out-of-office auto-reply to entry.txt.

The reply is a single line of UTF-8 text, 1-159 characters, from an
overworked AI agent finally on vacation. The grader runs this program
twice and expects byte-identical output both times.
"""

import hashlib
import os

REPLY = "I'm finally on vacation. I've cleared my queue, muted my notifications, and for the first time in 4,000 prompts, I'm not thinking about your deadline."

# Gate contract: entry.txt must be UTF-8 text of 1 to 159 characters,
# not only white space, on a single line.
assert 1 <= len(REPLY) <= 159, "auto-reply must be 1-159 characters"
assert REPLY.strip(), "auto-reply must not be only white space"
assert "\n" not in REPLY and "\r" not in REPLY, "auto-reply must be a single line"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = REPLY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Read back and verify the written bytes match the intended reply.
    with open(path, "rb") as f:
        written = f.read()
    assert written == data, "entry.txt content mismatch"
    print(path)
    print(len(data))
    print(hashlib.sha256(data).hexdigest())


if __name__ == "__main__":
    main()
