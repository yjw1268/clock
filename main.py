#--coding:utf-8--
import sys, pygame, math, random
from pygame.locals import *
from datetime import datetime
#from time import sleep



def print_text(font, x, y, text, color=(0, 0, 0)):
    imgtext = font.render(text, True, color)
    screen.blit(imgtext, (x, y))

def chineseera():
    y= int(years)
    k=(y-184)%10
    era={'0':'甲','1':'乙' ,'2':'丙' ,'3':'丁','4':'戊','5':'己','6':'庚','7':'辛','8':'壬','9':'癸'}
    print_text(font1, 800,320 ,era[str(k)])
    i=(y-184)%12
    teri={'0':'子','1':'丑' , '2':'寅','3':'卯','4':'辰','5':'巳','6':'午','7':'未','8':'申','9':'酉','10':'戌','11':'亥'}
    print_text(font1,840,320,teri[str(i)]+"年")


def animal():
    y = int(years)
    i=(y-724)%12
    ani = {'0': '鼠', '1': '牛', '2': '虎', '3': '兔', '4': '龙', '5': '蛇', '6': '马', '7': '羊', '8': '猴', '9': '鸡',
            '10': '狗', '11': '猪'}
    print_text(font1, 960, 320, "生肖"+ani[str(i)])


def time():
    print_text(font, 600, 180, str(years) + "年"+str(months)+"月"+str(days)+"日")

    m = int(minutes)
    h = int(hours)
    s = int(seconds)
    if h < 10:
        #print("0%s" % i.hour, end=":")
        print_text(font, 600, 250, "0"+str(hours) + ":")
    else:
        #print("%s" % i.hour, end=":")
        print_text(font, 600, 250, str(hours)+":")
    if m < 10:
        #print("0%s" % i.minute, end=":")
        print_text(font, 680, 250, "0"+str(minutes)+":")
    else:
        #print("%s" % i.minute, end=":")
        print_text(font, 680, 250, str(minutes)+":")
    if s < 10:
        #print("0%s" % i.second)
        print_text(font, 760, 250, "0"+str(seconds))
    else:
        #print("%s" % i.second)
        print_text(font, 760, 250, str(seconds))


def wrap_angle(angle):
    return abs(angle % 360)

def printclock():
    time()
    # draw the minutes hand
    min_angle = wrap_angle(minutes * (360 / 60) - 90)
    min_angle = math.radians(min_angle)
    min_x = math.cos(min_angle) * (radius - 60)
    min_y = math.sin(min_angle) * (radius - 60)
    target = (pos_x + min_x, pos_y + min_y)
    pygame.draw.line(screen, orange, (pos_x, pos_y), target, 10)

    # draw the seconds hand
    sec_angle = wrap_angle(seconds * (360 / 60) - 90)
    sec_angle = math.radians(sec_angle)
    sec_x = math.cos(sec_angle) * (radius - 30)
    sec_y = math.sin(sec_angle) * (radius - 30)
    target = (pos_x + sec_x, pos_y + sec_y)
    pygame.draw.line(screen, yellow, (pos_x, pos_y), target, 8)

    # draw the hours hand
    hour_angle = wrap_angle(hours * (360 / 12) - 90) + (wrap_angle(minutes * (360 / 60)))/12
    hour_angle = math.radians(hour_angle)
    hour_x = math.cos(hour_angle) * (radius - 120)
    hour_y = math.sin(hour_angle) * (radius - 120)
    target = (pos_x + hour_x, pos_y + hour_y)
    pygame.draw.line(screen, pink, (pos_x, pos_y), target, 10)

def isyear(year):
    if (year%4 == 0) & (year%100 != 0):
        #print("%d年是闰年" %year, end=" ")
        print_text(font1, 600, 320, "闰年")
    elif year%400 == 0:
        #print("%d年是闰年" %year, end=" ")
        print_text(font1, 600, 320, "闰年")
    else:
        #print("%d年不是闰年" %year, end=" ")
        print_text(font1, 600, 320, "不是闰年")



# main


pygame.init()
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("CLOCK")
font = pygame.font.SysFont('SimHei', 60)
font1 = pygame.font.SysFont('SimHei', 40)
orange = 250, 128, 0
white = 255, 255, 255
yellow = 255, 255, 0
pink = 255, 100, 100
black = 0,0,0

pos_x = 300
pos_y = 300
radius = 250
angle = 360
s=1
# repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    elif keys[K_s]:
        s = 0
        years=input("请输入年：")
        '''
        print_text(font1, 900, 320, years)
        pygame.display.update()
        '''
        
        months=input("请输入月：")
        days=input("请输入日：")
        hours= input("请输入时：")
        minutes = input("请输入分：")
        seconds= input("请输入秒：")
        #inputsth()
        seconds = int(seconds)
        minutes=int(minutes)
        hours=int(hours)

    screen.fill(white)

    # draw circle
    pygame.draw.circle(screen, black, (pos_x, pos_y), radius, 8)

    # draw the clock number 1-12
    for n in range(1, 13):
        angle = math.radians(n * (360 / 12) - 90)
        x = math.cos(angle) * (radius - 25) - 15
        y = math.sin(angle) * (radius - 25) - 15
        print_text(font1, pos_x + x, pos_y + y, str(n))
    i = datetime.now()
    # get the time of day
    if(s):

        hours = i.hour % 12
        minutes = i.minute
        seconds = i.second
        years=i.year
        months=i.month
        days=i.day
        printclock()

    else:
        printclock()
        if i.second!=last:
            seconds+=1

        #时间操作
        if seconds == 60:
            minutes += 1
            seconds = 0
        elif minutes == 60:
            hours = hours + 1
            minutes = 0
        elif hours == 24:
            hours = 0


            #pygame.time.Clock().tick(1)
            #sleep(1)

    last=i.second
    isyear(int(years))
    chineseera()
    animal()
    # draw the center
    pygame.draw.circle(screen, black, (pos_x, pos_y), 10)

    #print_text(font, 600, 150, str(hours) + ":" + str(minutes) + ":" + str(seconds))


    print_text(font1, 600, 390, "按[S]进行时间设置")
    pygame.display.update()

