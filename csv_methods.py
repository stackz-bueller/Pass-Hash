import csv

class DatabaseEngine():
  def __init__(self):
    self.File = 'Database/user-pass.csv'

  def push_user_info(self, info):
    with open(self.File, 'w', newline='') as csvfile:
        infowriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        infowriter.writerow(info)

  def pull_user_hash(self, username):
    reader = csv.reader(open(self.File, 'r'))
    for data in reader:
      if(username == data.username):
        return data.hash


