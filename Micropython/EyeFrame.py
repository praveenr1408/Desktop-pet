import framebuf
from ImageData import EyeReaction as er

#square eye frame 34x34
squareEyeFrame = framebuf.FrameBuffer(er.squareEye, 34, 34, framebuf.MONO_HLSB)

#round eye frame 34x34
roundEyeFrame = framebuf.FrameBuffer(er.roundEye, 34, 34, framebuf.MONO_HLSB)

#eye lid sad ledt frame 34x34
eyeLidSadLeftFrame = framebuf.FrameBuffer(er.eyeLidSadLeft, 34, 34, framebuf.MONO_HLSB)

#eye lid sad right frame 34x34
eyeLidSadRightFrame = framebuf.FrameBuffer(er.eyeLidSadRight, 34, 34, framebuf.MONO_HLSB)

#eye lid angry left frame 34x34
eyeLidAngryLeftFrame = framebuf.FrameBuffer(er.eyeLidAngryLeft, 34, 34, framebuf.MONO_HLSB)

#eye lid angry right frame 34x34
eyeLidAngryRightFrame = framebuf.FrameBuffer(er.eyeLidAngryRight, 34, 34, framebuf.MONO_HLSB)

#eye lid normal frame 34x34
eyeLidNormalFrame = framebuf.FrameBuffer(er.eyeLidNormal, 34, 34, framebuf.MONO_HLSB)

#eye lid happy frame 34x34
eyeLidHappyFrame = framebuf.FrameBuffer(er.eyeLidHappy, 34, 34, framebuf.MONO_HLSB)

#eye lid sleep left frame 34x34
eyeLidSleepLeftFrame = framebuf.FrameBuffer(er.eyeLidSleepLeft, 34, 34, framebuf.MONO_HLSB)

#eye lid sleep right frame 34x34
eyeLidSleepRightFrame = framebuf.FrameBuffer(er.eyeLidSleepRight, 34, 34, framebuf.MONO_HLSB)

#sleep Z1 8x10
SleepZ1Frame = framebuf.FrameBuffer(er.SleepZ1, 8, 10, framebuf.MONO_HLSB)

#sleep Z2 8x10
SleepZ2Frame = framebuf.FrameBuffer(er.SleepZ2, 8, 10, framebuf.MONO_HLSB)

#sleep Z3 8x10
SleepZ3Frame = framebuf.FrameBuffer(er.SleepZ3, 8, 10, framebuf.MONO_HLSB)


