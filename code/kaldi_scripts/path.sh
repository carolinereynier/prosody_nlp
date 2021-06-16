#export KALDI_ROOT=/afs/inf.ed.ac.uk/group/teaching/asr/tools/kaldi-ubuntu
export KALDI_ROOT=/afs/inf.ed.ac.uk/group/msc-projects/s2125019/prosody_nlp/kaldi

#export KALDI_ROOT=/afs/inf.ed.ac.uk/group/project/prosody/kaldi
export PATH=$PWD/utils/:$KALDI_ROOT/tools/openfst/bin:$PWD:$PATH
[ ! -f $KALDI_ROOT/tools/config/common_path.sh ] && echo >&2 "The standard file $KALDI_ROOT/tools/config/common_path.sh is not present -> Exit!" && exit 1
. $KALDI_ROOT/tools/config/common_path.sh

export LC_ALL=C
