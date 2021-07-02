#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    raw_feats_dir = sys.argv[1]
    augmentation = sys.argv[2]
    with open(f"{raw_feats_dir}/../train_text","r") as t:
        train_val_text = t.readlines()
    with open(f"{raw_feats_dir}/../test_text","r") as t:
        test_text = t.readlines()
    text_dict = dict()
    for text in train_val_text + test_text:
        k,v = text.split(" ",1)
        text_dict[k] = v.strip()

    for dataset in ["train","val","test"]:
        with open(f"{raw_feats_dir}/{dataset}.scp","r") as s:
            scps = s.readlines()
        texts = []
        utts = []
        scps_ = []
        for s in scps:
            u,p = s.split(" ",1)
            # if augmentation == "True" and dataset == "train":
            texts.append(text_dict[u.split("aug_")[0]])
            utts.append(u)
            scps_.append(s)

        dataset_dir = f"data/{dataset}"
        scps = scps_
        n_utts = len(scps)

        spk2utt = "Larry " + " ".join(utts)
        utt2spk = []
        wav = []

        for i in range(n_utts):
            utt2spk.append(utts[i] + " Larry\n")
            wav.append(utts[i] + " " + str(i) + ".wav\n")
        with open(dataset_dir + "/feats.scp", "w") as s:
            s.writelines(scps)
        with open(dataset_dir + "/text", "w") as t:
            for i in range(n_utts):
                t.write(f"{utts[i]} {texts[i]}\n")
        with open(dataset_dir + "/spk2utt", "w") as s:
            s.writelines(spk2utt)
        with open(dataset_dir + "/utt2spk", "w") as u:
            u.writelines(utt2spk)
        with open(dataset_dir + "/wav.scp", "w") as w:
            w.writelines(wav)
        
