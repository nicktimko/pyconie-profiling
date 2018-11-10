c.NotebookApp.port = 12345
c.NotebookApp.notebook_dir = "."

c.NotebookApp.password = "sha1:3d5189842c88:13478bb59c46a27c678573024be231c64b313f34"
# they don't use PBKDF2 w/ rounds? meh...  crack this, it's not hard.

c.NotebookApp.open_browser = False
c.NotebookApp.quit_button = False

c.KernelSpecManager.ensure_native_kernel = False
