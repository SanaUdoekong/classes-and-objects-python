class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.tracks = tracks
        self.score = score
        self.name = name
        self.age = age
        print("\n Student: \nName: ", name, "\n Age: ", age, "\n Tracks: ", tracks, "\n Score: ", score)

    #change name function
    def change_name(self, name):
        self.name =  name
        print("\nYour name has been changed to ", name)
    
    def change_age(self, age):
        self.age = age
        print("\nYour age has been changed to ", age)

    def add_track(self, track):
        self.tracks.append(track)
        print('\n', track, " successfully added!")

    def get_score(self):
        print("\nYour score is ", self.score)



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
