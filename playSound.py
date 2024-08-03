import pygame
import multitasking
import time
from UIdate import date

pygame.mixer.init()  # 初始化混音器模块
channels_voice = []
channels_music = []

@multitasking.task
def voice_change(cnt, initialize):
    voices = []  # 当前播放的语音，index只有0
    voice = pygame.mixer.Sound("sounds/" + str(date["voice"][cnt]) + ".mp3")
    voices.append(voice)  # 把音频添加进播放列表

    channels_voice.clear()  # 清空全局 channels_voice 列表

    for voice in voices:
        channel = voice.play()  # 播放
        channels_voice.append(channel)

    if initialize == "start":#为了保证旧版本channels_voice的初始化，现阶段无用，只为了保证程序的完整性
        return

    # 等待音频播放结束
    while any(channel.get_busy() for channel in channels_voice):
        time.sleep(0.1)
        pass

@multitasking.task
def music_change(cnt, initialize):
    global channels_music

    musics = []  # 当前播放的音乐，index只有0
    music_path = "sounds/" + date["music"][cnt] + ".mp3"
    musics.append(music_path)  # 把音频路径添加进播放列表

    channels_music.clear()  # 清空全局 channels_music 列表

    for music in musics:
        pygame.mixer.music.load(music)  # 加载音乐
        pygame.mixer.music.play(loops=-1)  # 播放音乐，循环播放

    if initialize == "start":#为了保证旧版本channels_music的初始化，现阶段无用，只为了保证程序的完整性
        return

def voice_stop():
    # 停止已经播放的音频
    for channel in channels_voice:
        channel.stop()

def music_stop():
    # 停止已经播放的音频
    pygame.mixer.music.stop()  # 停止音乐播放
    for channel in channels_music:
        channel.stop()