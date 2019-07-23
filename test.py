import ffmpegu as fu

v = '/data/rvsn/vp/data/marmoset/rgbda_record_data/20181113/recording-2016-12-31_19_34_46.mp4'
print( fu.VideoGetWidthHeight(v) )
print( fu.VideoGetNumFrames(v) )
print( fu.VideoGetNumSeconds(v) )
print( fu.VideoExtractFrame(v, 'test.jpg', 100.5) )

res = fu.VideoExtractFramesEvenlySpaced(v, 'test', 10)
print(res)
