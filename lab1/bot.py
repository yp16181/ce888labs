from sopel import module
from emo.wdemotions import EmotionDetector
global ave
ave = 0
emo = EmotionDetector()

@module.rule('')
def hi(bot, trigger):
    global ave
    a = 0.1
    ave = ave + a *(emo.detect_emotion_in_raw_np(str(trigger)) - ave)
    print(trigger, trigger.nick)
    #bot.say('Hi, ' + trigger.nick)
    print(ave)
