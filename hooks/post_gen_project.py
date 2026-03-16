import os
import shutil

# The generated project dir is the CWD at hook time
project_dir = os.path.abspath(os.curdir)

parent_dir = os.path.dirname(project_dir)
# Move all contents up to the parent
for item in os.listdir(project_dir):
    shutil.move(os.path.join(project_dir, item), os.path.join(parent_dir, item))

# Remove the now-empty intermediate folder
os.rmdir(project_dir)
