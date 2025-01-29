import draw, random

def in_internal(internal: tuple, num: int):
    return ((internal[0] <= num) and (internal[1] >= num))

class Note:
    def __init__(self, left, right):
        self.l_bound = left
        self.r_bound = right
        if left != right:
            self.color = draw.COL_MULTI
        elif (left & 1):
            self.color = draw.COL_ODD
        else:
            self.color = draw.COL_EVEN
        self.positionY = 0
    
    def move(self):
        self.positionY += draw.NOTE_SPEED
        if self.positionY > draw.GREAT_INTERNAL[1]:
            return 'FAIL'
        return 'NULL'
    
    def judge(self):
        if in_internal(draw.PERFECT_INTERNAL, self.positionY):
            return 'PERFECT'
        elif in_internal(draw.GREAT_INTERNAL, self.positionY):
            return 'GREAT'
        elif in_internal(draw.FAIL_INTERNAL, self.positionY):
            return 'FAIL'
        return 'ERROR'
    
    
last_note_track_id = -1

def summon_note() -> list:
    global last_note_track_id
    track_id = random.randint(0, 3)
    while (track_id == last_note_track_id):
        track_id = random.randint(0, 3)
    last_note_track_id = track_id
    return [Note(track_id, track_id)]

switch = 0

def summon_note2() -> list:
    global switch
    switch ^= 1
    if switch:
        track_id = random.randint(0, 3)
        note_list = []
        for i in range(0, 4):
            if i != track_id:
                note_list.append(Note(i, i))
        return note_list
    else:
        return []
    
NoteType = Note