import pygame, draw, note, sys, time
from collections import deque

# 50fps 5f/note -> BPM 150 16'

pygame.init()
draw.screen = screen = pygame.display.set_mode(size = draw.WINDOWS_SIZE)
pygame.display.set_caption('In Yo')
fclock = pygame.time.Clock()

keys = (pygame.K_d, pygame.K_f, pygame.K_j, pygame.K_k)

def main():
    notes = deque([])
    partiples = deque([])
    current_time = 0
    hp = draw.HIGH_HP
    score = 0

    draw.draw_clear()
    draw.draw_judgeline()
    draw.draw_hp(hp)
    time.sleep(1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == keys[0]:
                    for _note in notes:
                        if note.in_internal((_note.l_bound, _note.r_bound), 0):
                            if note.in_internal(draw.FAIL_INTERNAL, _note.positionY):
                                exit_code = _note.judge()
                                # print(f'note judgement code:{exit_code}')
                                if exit_code == 'PERFECT':
                                    partiples.append(draw.Partiple('PERFECT', 0, current_time))
                                    hp += draw.PERFECT_DHP
                                    score += draw.PERFECT_DSC
                                elif exit_code == 'GREAT':
                                    partiples.append(draw.Partiple('GREAT', 0, current_time))
                                    hp += draw.GREAT_DHP
                                    score += draw.GREAT_DSC
                                elif exit_code == 'FAIL':
                                    partiples.append(draw.Partiple('FAIL', 0, current_time))
                                    hp += draw.FAIL_DHP
                                notes.remove(_note)
                            break
                elif event.key == keys[1]:
                    for _note in notes:
                        if note.in_internal((_note.l_bound, _note.r_bound), 1):
                            if note.in_internal(draw.FAIL_INTERNAL, _note.positionY):
                                exit_code = _note.judge()
                                # print(f'note judgement code:{exit_code}')
                                if exit_code == 'PERFECT':
                                    partiples.append(draw.Partiple('PERFECT', 1, current_time))
                                    hp += draw.PERFECT_DHP
                                    score += draw.PERFECT_DSC
                                elif exit_code == 'GREAT':
                                    partiples.append(draw.Partiple('GREAT', 1, current_time))
                                    hp += draw.GREAT_DHP
                                    score += draw.GREAT_DSC
                                elif exit_code == 'FAIL':
                                    partiples.append(draw.Partiple('FAIL', 1, current_time))
                                    hp += draw.FAIL_DHP
                                notes.remove(_note)
                            break
                elif event.key == keys[2]:
                    for _note in notes:
                        if note.in_internal((_note.l_bound, _note.r_bound), 2):
                            if note.in_internal(draw.FAIL_INTERNAL, _note.positionY):
                                exit_code = _note.judge()
                                # print(f'note judgement code:{exit_code}')
                                if exit_code == 'PERFECT':
                                    partiples.append(draw.Partiple('PERFECT', 2, current_time))
                                    hp += draw.PERFECT_DHP
                                    score += draw.PERFECT_DSC
                                elif exit_code == 'GREAT':
                                    partiples.append(draw.Partiple('GREAT', 2, current_time))
                                    hp += draw.GREAT_DHP
                                    score += draw.GREAT_DSC
                                elif exit_code == 'FAIL':
                                    partiples.append(draw.Partiple('FAIL', 2, current_time))
                                    hp += draw.FAIL_DHP
                                notes.remove(_note)
                            break
                elif event.key == keys[3]:
                    for _note in notes:
                        if note.in_internal((_note.l_bound, _note.r_bound), 3):
                            if note.in_internal(draw.FAIL_INTERNAL, _note.positionY):
                                exit_code = _note.judge()
                                # print(f'note judgement code:{exit_code}')
                                if exit_code == 'PERFECT':
                                    partiples.append(draw.Partiple('PERFECT', 3, current_time))
                                    hp += draw.PERFECT_DHP
                                    score += draw.PERFECT_DSC
                                elif exit_code == 'GREAT':
                                    partiples.append(draw.Partiple('GREAT', 3, current_time))
                                    hp += draw.GREAT_DHP
                                    score += draw.GREAT_DSC
                                elif exit_code == 'FAIL':
                                    partiples.append(draw.Partiple('FAIL', 3, current_time))
                                    hp += draw.FAIL_DHP
                                notes.remove(_note)
                            break
        
        if (current_time % draw.NEXT_NOTE_APPEAR_TIME == 0):
            note_list = note.summon_note()
            for _note in note_list:
                notes.append(_note)
        
        pop_cnt = 0
        for _note in notes:
            exit_code = _note.move()
            if exit_code == 'FAIL':
                partiples.append(draw.Partiple('FAIL', _note.l_bound, current_time))
                hp += draw.FAIL_DHP
                pop_cnt += 1
        
        for _ in range(pop_cnt):
            notes.popleft()

        if hp > 100:
            hp = 100
        elif hp < 0:
            break

        pop_cnt = 0
        for _partiple in partiples:
            if current_time - _partiple.start_time > draw.PARTIPLE_LAST_TIME:
                pop_cnt += 1
            else:
                break
        
        for _ in range(pop_cnt):
            partiples.popleft()

        draw.draw_clear()
        draw.draw_judgeline()
        draw.draw_hp(hp)
        draw.draw_text(draw.encode_score(score), draw.COL_WHITE, 30, (10, 10))
        for _note in notes:
            draw.draw_note(_note)
        for _partiple in partiples:
            _partiple.draw()

        pygame.display.update()
        fclock.tick(50)
        current_time += 1

    draw.draw_clear()
    draw.draw_text('GAME OVER', draw.COL_WHITE, 75, (draw.WIDTH // 2 - 150, draw.HEIGHT // 2 - 50))
    draw.draw_text('Your score:' + draw.encode_score(score), draw.COL_WHITE, 35, (draw.WIDTH // 2 - 150, draw.HEIGHT // 2 + 40))
    pygame.display.update()
    time.sleep(3)
    pygame.quit()

if __name__ == '__main__':
    main()