import sqlite3

connec = sqlite3.connect('video_manager.db')
cursor = connec.cursor()

# Creating Table
cursor.execute('''
   CREATE TABLE IF NOT EXISTS videos (
         id INTEGER PRIMARY KEY,
         name TEXT NOT NULL,
         time NOT NULL
   )
''')

def list_videos():
   cursor.execute("SELECT * FROM videos") # returns tuple
   print("\n-------------------------------------------------------------")
   
   for row in cursor.fetchall():
      print(row)
      
   print("\n-------------------------------------------------------------")
      
def add_video(name, time):
   cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
   connec.commit()
   
def update_video(vid_id, new_name, new_time):
   cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, vid_id))
   connec.commit()

def delete_video(vid_id):
   cursor.execute("DELETE FROM videos WHERE id = ?", (vid_id,)) #tuple

def main():
   while True:
      print("\n******* Youtube manager app *******")
      print("1. List Videos")
      print("2. Add Videos")
      print("3. Update Videos")
      print("4. Delete Videos")
      print("5. Terminate app")
      
      choice = input("\nEnter your choice : ")
      
      
      if choice == '1':
         list_videos()
         
      elif choice == '2':
         name = input("Enter video name : ")
         time = input("Enter video duration : ")
         add_video(name, time)
         
      elif choice == '3':
         vid_id = input("Enter video ID to update : ")
         name = input("Enter video name : ")
         time = input("Enter video duration : ")
         update_video(vid_id, name, time)
         
      elif choice == '4':
         vid_id = input("Enter video ID to delete : ")
         delete_video(vid_id)
         
      elif choice == '5':
         break
      
      else:
         print("Invalid choice!")
   
   connec.close()
         
if __name__ == '__main__':
   main()