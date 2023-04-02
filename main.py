import os
import pygame




if __name__ == "__main__":
    pygame.init()
    X = 838
    Y = 489

    screen = pygame.display.set_mode((X, Y))
    pygame.display.set_caption("image")

    path = "./flags"
    flags = os.listdir(path)
    status = True
    while status:

        for i in pygame.event.get():
            for flag in flags:
                path_flag = path + "/" + flag
                flag_name = flag.replace(".jpeg", "")
                flag_img = pygame.image.load(path_flag).convert()
                print(flags)

                screen.blit(flag_img, (0, 0))
                pygame.display.flip()

                answer = input("Whom is this flag? \n")
                if answer.lower() == flag_name:
                    print("Correct answer!")
                    flags.remove(flag)

                    if not flags:
                        print("Congratulations")
                        status = False
            
                else:
                    print("That's incorrect")
                
                if i == pygame.QUIT:
                    status = False
                
    
    pygame.quit()