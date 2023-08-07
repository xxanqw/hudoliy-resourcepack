import hashlib

def get_sha1(file_name):
  """Returns the SHA1 hash of the file."""
  with open(file_name, "rb") as f:
    sha1 = hashlib.sha1()
    for chunk in iter(lambda: f.read(4096), b""):
      sha1.update(chunk)
  return sha1.hexdigest()

if __name__ == "__main__":
  sha1 = get_sha1("pack.zip")
  with open("sha1.txt", "w") as f:
    f.write(sha1)
