__version__ = '0.1'
from subprocess import check_output as co, run
from functools import partial
import numpy as np
import du

def VideoGetWidthHeight(_file):
  cmd = f'ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 "{_file}"'
  out = _run(cmd)
  w, h = out.strip().split('x')
  return int(w), int(h)

def VideoGetNumFrames(_file):
  cmd = f'ffprobe -v error -select_streams v:0 -show_entries stream=nb_frames -of default=nokey=1:noprint_wrappers=1 "{_file}"'
  out = _run(cmd)
  return int(out.strip())

def VideoGetNumSeconds(_file):
  cmd = f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{_file}"'
  out = _run(cmd)
  return float(out.strip())

def VideoExtractFrame(_file, outImg, seconds, **kwargs):
  qscale = kwargs.get('qscale', 2)
  cmd = f'ffmpeg -ss {seconds} -i "{_file}" -vframes 1 -y -loglevel quiet -q:v {qscale} {outImg}'
  out = run(cmd, shell=True)
  return out.returncode

def VideoExtractFramesEvenlySpaced(_file, outPath, nFrames, **kwargs):
  outPrefix = kwargs.get('outPrefix', du.fileparts(_file)[1] + '-')
  outCountFmt = kwargs.get('outCountFmt', '08d')
  outSuffix = kwargs.get('outSuffix', 'jpg')
  qscale = kwargs.get('qscale', 2)

  nSeconds = VideoGetNumSeconds(_file)
  times = np.linspace(0.1, nSeconds-0.1, nFrames)
  names = [ f'{outPath}/{outPrefix}{n:{outCountFmt}}.{outSuffix}' for n in range(nFrames) ]

  if kwargs.get('parallel', True):
    f = partial(VideoExtractFrame, _file, qscale=qscale)
    args = [ (names[n], times[n]) for n in range(nFrames) ]
    res = du.Parfor(f, args)
    return res
  else:
    rc = 0
    for n in range(nFrames):
      rc += VideoExtractFrame(_file, names[n], times[n], qscale=qscale)
    return rc

def _bytes2str(b): return b.decode('utf-8')
def _run(cmd): return _bytes2str(co(cmd, shell=True))
