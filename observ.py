import os, time
path_to_watch = "."
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
  time.sleep (1)
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]
  removed = [f for f in before if not f in after]
  if added:
      print "Added: ", ", ".join (added)
      for k in added:
        os.system("python crop.py "+k)
  if removed:
      print "Removed: ", ", ".join (removed)
  before = after
