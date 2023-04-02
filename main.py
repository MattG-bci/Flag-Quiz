import os
import pygame


if __name__ == "__main__":
    pygame.init()
    X = 1280
    Y = 780

    screen = pygame.display.set_mode((X, Y))
    pygame.display.set_caption("image")

    path = "./flags"
    flags = os.listdir(path)
    status = True

    correct = 0
    incorrect = 0
    n_flags = len(flags)
    while status:

        for i in pygame.event.get():
            for flag in flags:
                path_flag = path + "/" + flag
                flag_name = flag.replace(".jpeg", "")
                flag_img = pygame.image.load(path_flag).convert()

                screen.blit(flag_img, (280, 20))
                pygame.display.flip()

                answer = input("Whom is this flag? \n")
                if answer.lower() == flag_name:
                    print("Correct answer!")
                    correct += 1
                    flags.remove(flag)

                    if not flags:
                        print("Congratulations! You have guessed all the flags!")
                        print(f"Your score is: {(correct/(n_flags + incorrect) * 100):.3f}%")
                        status = False
            
                else:
                    print("That's incorrect")
                    incorrect += 1
                
                if i == pygame.QUIT:
                    status = False
                
    
    pygame.quit()