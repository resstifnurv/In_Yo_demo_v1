import pygame, note

COL_ODD, COL_EVEN, COL_MULTI = (255,255,255), (250,128,114), (0,255,127)
COL_WHITE, COL_BLACK = (255,255,255), (0,0,0)
COL_PERFECT, COL_GREAT, COL_FAIL = (255,215,0), (127,255,0), (211,211,211)
COL_DEFAULT = (138,43,226)
COL_HIGH_HP, COL_MEDIUM_HP, COL_LOW_HP = (0,177,0), (177,177,0), (177,0,0)

WINDOWS_SIZE = WIDTH, HEIGHT = 400, 700
NOTE_HEIGHT, NOTE_WIDTH = 20, 85
JUDGELINE_POSITIONY, JUDGELINE_HEIGHT = 600, 3

PARTIPLE_ABOVE_HEIGHT = 50
PARTIPLE_LAST_TIME = 50

FPS, BPM = 50, 150
NEXT_NOTE_APPEAR_TIME = FPS // (BPM // 15)

NOTE_SPEED = 18
APPEAR_TIME = JUDGELINE_POSITIONY // NOTE_SPEED

PERFECT_INTERNAL = (JUDGELINE_POSITIONY - (0.06 * FPS * NOTE_SPEED),
                    JUDGELINE_POSITIONY + (0.06 * FPS * NOTE_SPEED))
GREAT_INTERNAL = (JUDGELINE_POSITIONY - (0.11 * FPS * NOTE_SPEED),
                    JUDGELINE_POSITIONY + (0.11 * FPS * NOTE_SPEED))
FAIL_INTERNAL = (JUDGELINE_POSITIONY - (0.15 * FPS * NOTE_SPEED),
                    JUDGELINE_POSITIONY + (0.15 * FPS * NOTE_SPEED))

TRACK_INTERNAL = ((0, NOTE_WIDTH),
                  (NOTE_WIDTH + 1, 2 * NOTE_WIDTH),
                  (2 * NOTE_WIDTH + 1, 3 * NOTE_WIDTH),
                  (3 * NOTE_WIDTH + 1, 4 * NOTE_WIDTH))

MAX_HP = 100
HIGH_HP, LOW_HP = MAX_HP * 7 // 10, MAX_HP * 3 // 10
PIX_PER_HP = HEIGHT // MAX_HP
PERFECT_DHP, GREAT_DHP, FAIL_DHP = 2, 1, -8
PERFECT_DSC, GREAT_DSC, FAIL_DSC = 500, 250, 0

screen: pygame.Surface

def draw_clear():
    screen.fill(COL_BLACK)

def draw_judgeline():
    pygame.draw.rect(
        surface=screen,
        color=COL_WHITE,
        rect=pygame.Rect(
            0,
            JUDGELINE_POSITIONY,
            WIDTH,
            JUDGELINE_HEIGHT,
        )
    )

def draw_note(_note: note.Note):
    pygame.draw.rect(
        surface=screen,
        color=_note.color,
        rect=pygame.Rect(
            TRACK_INTERNAL[_note.l_bound][0],
            _note.positionY - NOTE_HEIGHT,
            TRACK_INTERNAL[_note.r_bound][1] - TRACK_INTERNAL[_note.l_bound][0],
            NOTE_HEIGHT
        )
    )

def draw_hp(hitpoint):
    color = COL_LOW_HP
    if hitpoint >= HIGH_HP:
        color = COL_HIGH_HP
    elif hitpoint >= LOW_HP:
        color = COL_MEDIUM_HP
    pygame.draw.rect(
        surface=screen,
        color=color,
        rect=pygame.Rect(
            TRACK_INTERNAL[3][1] + 1,
            HEIGHT - hitpoint * PIX_PER_HP,
            WIDTH - TRACK_INTERNAL[3][1] - 1,
            hitpoint * PIX_PER_HP
        )
    )

def draw_text(text, color, size, position):
    font = pygame.font.SysFont('思源黑体CN', size)
    message = font.render(text, True, color)
    screen.blit(message, position)

def encode_score(score):
    s_list = list(str(score).zfill(7))
    s_list.insert(4, '\'')
    s_list.insert(1, '\'')
    return ''.join(s_list)

class Partiple:
    def __init__(self, status, track_id, start_time):
        self.status = status
        self.track_id = track_id
        self.start_time = start_time

    def draw(self):
        font = pygame.font.SysFont('思源黑体CN', 25)
        position = (TRACK_INTERNAL[self.track_id][0] + NOTE_WIDTH // 5, JUDGELINE_POSITIONY - PARTIPLE_ABOVE_HEIGHT)
        color = COL_DEFAULT
        if self.status == 'PERFECT':
            color = COL_PERFECT
        elif self.status == 'GREAT':
            color = COL_GREAT
        elif self.status == 'FAIL':
            color = COL_FAIL
        message = font.render(self.status, True, color)
        screen.blit(message, position)