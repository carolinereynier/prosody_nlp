""" Script to transform Kaldi transcriptions so they are in the same format as t
he official Switchboard transcriptions """

import os
import sys
import re

def read_file(kaldi_trans, output_file):
    line_counter=1
    old_start_time=0.0
    old_end_time=0.0
    with open(kaldi_trans, "r") as kaldi_input:
        with open(output_file, "w") as output:
            for line in kaldi_input:
                new_line=line.replace('0', '', 1)
                new_line=new_line.replace('-', '', 1)
                new_line=new_line.replace('_', ' ', 1)
                new_line=new_line.replace('-', ' ', 2)
                new_line_list=new_line.split(' ')
                start_time=float(new_line_list[1])/100
                end_time=float(new_line_list[2])/100
                if start_time > old_end_time:
                    turn_id=new_line_list[0]+"-ms98-a-"+str(line_counter).zfill(4)
                    added_line=str(turn_id)+" "+str(old_end_time)+" "+str(start_time)+ " " + "[silence]"+"\n"
                    output.write(added_line)
                    line_counter+=1
                #new_line=re.sub(r'sw[0-9]{5}-[AB]_[0-9]{6}-[0-9]{6} [^\n]*', r'sw[0-9]{5}[AB] [0-9]{6} [0-9]{6} [^\n]*', line)
                turn_id=new_line_list[0]+"-ms98-a-"+str(line_counter).zfill(4)
                new_line_list[0]=str(turn_id)
                new_line_list[1]=str(start_time)
                new_line_list[2]=str(end_time)
                new_line=' '.join(new_line_list)
                output.write(new_line)
                line_counter+=1
                old_start_time=start_time
                old_end_time=end_time
    kaldi_input.close()
    output.close()

if __name__ == '__main__':
    kaldi_trans = '/disk/scratch/s2125019/prosody_nlp/kaldi-master2/egs/swbd/s5c/exp/tri4/decode_dev_sw1_tg.si/scoring/text.filt'
    output_dir = '/disk/scratch/s2125019/prosody_nlp/preprocessing_output.text'
    read_file(kaldi_trans, output_dir)

