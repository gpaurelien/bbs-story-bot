import pyautogui as pag
import PIL
import time

class Bot:
    def findAndClick(self, path):
        # Will find the image, then click it. 
        # Returns false and terminates if nothing is found
        coords = pag.locateCenterOnScreen(path, confidence=0.8)

        if not coords:
            return False
        else:
            x, y = coords
            pag.click(x, y)
        
        return True
    
    def run(self):
        inMission = True # We consider starting the bot in a mission

        startFailed = auto = 0

        print('Press "Ctrl+C" for break the script')

        while 1: 
            if startFailed < 10:
                if inMission:
                    if self.findAndClick("assets\\auto.png") and not auto:
                        auto += 1
                        print('The bot is running...')
                        time.sleep(60) # Until the quest is over
                
                    elif self.findAndClick('assets\\skip.jpg'):
                        print('Conversation skipped')

                    elif self.findAndClick('assets\\friend_request.jpg'):
                        print('Friend requests handled')

                    elif self.findAndClick('assets\\touch_screen.jpg'):
                        print('Touch screeen action handled')

                    elif self.findAndClick("assets\\next_quest.png"):
                        inMission = False
                        time.sleep(5)

                else:
                    pag.click(x=1054, y=826)
                    
                    if self.findAndClick('assets\\skip.jpg'):
                        print('Conversation skipped')

                    elif self.findAndClick('assets\\prep_quest.jpg'):
                        time.sleep(5)

                    elif self.findAndClick('assets\\start_quest.jpg'):
                        inMission = True
                        time.sleep(5)

                    else:
                        print('The quest failed to start')
                        startFailed += 1
            else:
                return f'Bot get stucked'

if __name__ == '__main__':
    bot = Bot()
    bot.run()