import pandas as pd
import os

print(pd.__version__)

def extract_ids_from_time_file(infile,outfile):
    df = pd.read_csv(infile,header=None, sep='\t')

    with open(outfile,'w') as f:
        for i,row in df.iterrows():
            spk = row[1]
            conv,sent_num = row[2].split('~')
            sent_id = '_'.join((conv,spk,sent_num))
            f.write(sent_id)
            f.write('\n')

def main():
    in_dir = '/afs/inf.ed.ac.uk/group/msc-projects/s2125019/prosody_nlp/data/trees'
    out_dir = '/afs/inf.ed.ac.uk/group/msc-projects/s2125019/prosody_nlp/data/output_data/input_features'
    splits = ['train','dev','test']
    for spl in splits:
        extract_ids_from_time_file(os.path.join(in_dir,spl+'.times'),os.path.join(out_dir,spl+'_sent_ids.txt'))

if __name__=="__main__":
    main()
