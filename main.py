import pyautogui as pag
import PIL
import time

class Bot:
    def findAndClick(self, path):
        coords = pag.locateCenterOnScreen(path, confidence=0.8)

        if not coords:
            return False
        else:
            x, y = coords
            pag.click(x, y)
        
        return True
    
    def run(self):
        inMission = True

        startFailed = auto = 0

        print('Press "Ctrl+C" for break the script')

        while 1: 
            if startFailed < 10:
                if inMission:
                    if self.findAndClick("assets\\auto.png"):
                        if not auto:
                            auto += 1
                            print('The bot is running...')
                        
                        time.sleep(60) # waiting for the bot to complete the quest
                
                    elif self.findAndClick('assets\\skip.jpg'):
                        print('Conversation skipped')

                    elif self.findAndClick('assets\\friend_request.jpg'):
                        print('Friend requests handled')

                    elif self.findAndClick('assets\\touch_screen.jpg'):
                        print('Touch screen action handled')

                    elif self.findAndClick("assets\\next_quest.png"):
                        inMission = False
                        time.sleep(5)

                else:
                    pag.click(x=1054, y=826) # skip cinematic
                    
                    if self.findAndClick('assets\\skip.jpg'):
                        print('Conversation skipped')

                    elif self.findAndClick('assets\\prep_quest.jpg'):
                        print('Quest preparation handled')
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