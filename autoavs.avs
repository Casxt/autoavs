MP_Pipeline("""
V="Sasami[num].rmvb"
ASS="Sasami[num].ass"
FFIndex(V)
AudioDub(FFVideoSource(V,fpsnum=24000,fpsden=1001), FFAudioSource(V))
nnedi3_resize16(1280, 720, lsb_in=False, lsb=True)
### prefetch: 128, 64
### ###
LumaDBL(grain="AddGrainC(0.7)", g_lsb=false, g_lsb_in=false, lsb=true, lsb_in=true)
### prefetch: 64, 32
### ###
SMDegrain(lsb_in=true)
Convolution3d("animeHQ") 
### prefetch: 32, 16
### ###
aWarpSharp2(thresh=96, blur=2, type=0, depth=16, chroma=4)
TextSub(ASS)
### prefetch: 16, 8
""")